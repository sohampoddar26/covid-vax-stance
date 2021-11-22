# Libraries
import torch
from torchtext.data import Field, TabularDataset, Iterator

import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer, BertForSequenceClassification

import os
import csv
import time
import argparse
import warnings

torch.manual_seed(42)
warnings.filterwarnings('ignore')


#%% PARSE ARGUMENTS
CUDA_DEV = 'cuda:0' if torch.cuda.is_available() else 'cpu'


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("in_path", type=str, help="path to a CSV file or directory where the CSV files are stored")
parser.add_argument("--text_col", type=str, default="text", help="Header of the text column in the CSV files")

parser.add_argument("--out_dir", type=str, default=".", help="path to the directory where the predicted output files will be stored (default: same directory as the code file)")
parser.add_argument("--model_dir", type=str, default="./covid_vax_model/", help="path to the directory where the trained model is stored")

parser.add_argument("--device", type=str, default=CUDA_DEV, help="cuda device")

parser.add_argument("--max_seq_len", type=int, default=100, help="Maximum Sequence Length")
parser.add_argument("--batch_size", type=int, default=16, help="Batch Size")

args = parser.parse_args()

device = torch.device(args.device)
print("RUNNING ON DEVICE:", device)

INPATH = args.in_path
OUTDIR = args.out_dir

MODEL_PATH = args.model_dir

TEXT_COL_HEAD = args.text_col

MAX_SEQ_LEN = args.max_seq_len
BATCH_SIZE = args.batch_size



#%% INITTIALIZE TOKENIZER ***************************************************

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

PAD_INDEX = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
UNK_INDEX = tokenizer.convert_tokens_to_ids(tokenizer.unk_token)

# label_field = Field(sequential=False, use_vocab=False, batch_first=True, dtype=torch.float)
text_field = Field(use_vocab=False, tokenize=tokenizer.encode, lower=False, include_lengths=False, batch_first=True,
                   fix_length=MAX_SEQ_LEN, pad_token=PAD_INDEX, unk_token=UNK_INDEX)



#%% MODULES *****************************************************************

class BERT(nn.Module):
        def __init__(self):
                super(BERT, self).__init__()    
                self.encoder = BertForSequenceClassification.from_pretrained(MODEL_PATH, num_labels = 3)
        
        def forward(self, text, label= None):
                output = self.encoder(text, labels=label)[:2]
                if not label is None:
                        loss, text_fea = output
                else:
                        text_fea = output[0]
                        loss = None
            
                return loss, text_fea


classmap = ['Neutral', 'AntiVax', 'ProVax']

def predict(data_path, model): 
        model.eval()
        
        # READ CSV FILE AND CREATE AN ITERATOR
        with open(data_path) as fp:
                rdr = csv.reader(fp)
                txtcol = next(rdr).index(TEXT_COL_HEAD)
                fields = [(None, None)] * (txtcol) + [('text', text_field)]
                
        data = TabularDataset(data_path, format='CSV', fields = fields , skip_header = True)
        test_iter = Iterator(data, batch_size=BATCH_SIZE, device=device, train=False, shuffle=False, sort=False)
        
        
        # PREDICT CLASS PROBABILITIES AND COMPUTE STANCE        
        y_pred = []
        raw = []
        with torch.no_grad():
                for text, _ in test_iter:
                        text = text.type(torch.LongTensor)  
                        text = text.to(device)
                        output = model(text)
        
                        _, output = output
                        raw.extend(F.softmax(output, 1).tolist())
                        y_pred.extend(torch.argmax(output, 1).tolist())

        return [classmap[x] for x in y_pred], raw



#%% MAIN  *******************************************************************
model = BERT().to(device)
print("Model Loaded from:", MODEL_PATH)
print("Saving predicted files to:", OUTDIR)

if os.path.isfile(INPATH):
        INDIR, fn = os.path.split(INPATH)
        files = [fn]        
else:
        INDIR = INPATH
        files = sorted([f for f in next(os.walk(INDIR))[2]])

if not os.path.exists(OUTDIR):
        os.makedirs(OUTDIR)


for fn in files:
        t0 = time.time()
        print("\nCalculating for file:", fn, flush = True)
        path = os.path.join(INDIR, fn)
        preds, raw = predict(path, model)

        with open(path) as fp:
                rdr = csv.reader(fp)
                head = next(rdr)
                rdr = list(rdr)

                with open(os.path.join(OUTDIR, fn), 'w') as fo:
                        wrt = csv.writer(fo)
                        wrt.writerow(head + ['pred', 'p(Neutral)', 'p(AntiVax)', 'p(ProVax)'])
                        for row, pr, rs in zip(rdr, preds, raw):
                                wrt.writerow(row + [pr]+ [round(x, 4) for x in rs])
                                
        t1 = time.time()
        print("Completed in %0.1f mins"%((t1 - t0) / 60))
