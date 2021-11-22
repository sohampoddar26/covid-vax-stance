# COVID-19 vaccine stance classifier

## Introduction
This directory contains the code to run our vaccine-stance classifier model on a set of tweet texts (or any text) to determine if they are ProVax or AntiVax (described in the [dataset directory README](/dataset/README.md)). 
The classfier is based on covid-twitter-bert-v2 which is a finetuned version of the bert-large model. The model was then trained on 3 different datasets. For more details on the classifier model and its training please read our paper on [Arxiv](https://arxiv.org "Paper on Arxiv").


## Requirements
The saved classifier model is available at [this link](https://drive.google.com/ "Link to model"). You need to download this model directory before running the code. 

Packages required
- python==3.8
- pytorch==1.6
- torchtext==0.8
- transformers==4.1

*(**Note:** The `torchtext` version needs to be the same as we used some deprecated classes (might be updated in future). For others, the given versions are the ones that were used for development of our codes and higher versions should also be usable.)*

## Example Usage 
For details on the different arguments the code takes, you can run: 
```
python classifier_predict.py -h
```


Minimal example:
```
python classifier_predict.py sample_data/
```


With different arguments:
```
python classifier_predict.py ../dataset/our_data.csv  --text_col tweet  --out_dir predicted_dataset/  --model_dir covid_vax_model/  --device cuda:1
```


**WARNING:** The output files are saved with the same filenames as the input files, thus you should keep the directory of input file(s) different from the output directory (else the data will be replaced).

***Note:** In case you do not have enough GPU memory, you can reduce the `--max_seq_len` and `--batch_size` arguments. If you have lots of GPU memory and want to speed up computation, increase the `--batch_size`*


## Citation
If you use our classifier model, please cite the our paper as given in the [main README](/README.md) in the root directory.
