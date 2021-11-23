# COVID-19 vaccine Datasets

## Introduction
This directory contains datasets of tweets labelled into three classes according to their stance towards COVID-19 vaccines:- 
- **AntiVax:** the tweet is against the use of vaccines
- **ProVax:** the tweet is supporting the use of vaccines
- **Neutral:** Neither of the above


## Dataset Description
We have provided the tweet IDs, anonymized tweet texts and the corresponding labels in standard CSV formatted files. These can be read using any CSV reading tool, e.g. in Python, either of the "csv" or "pandas" libraries can be used. 

There are 3 CSV files in this directory:
- [Our dataset](our_labelled_data.csv)  from the paper consists of 1700 tweets on COVID-19 vaccines. Each tweet was labelled by three annotators on the crowdsourcing platform [Prolific](https://prolific.co "Prolific"). 1606 of these tweets have a majority label (at least two annotators agreed on the label).
For more details on the data collection and annotation process please read our paper on [Arxiv](https://arxiv.org/abs/2111.10667 "Paper on Arxiv") or from the root directory. 


- We had got some [additional data](our_labelled_data_additional.csv) annotated after submitting the paper, in the same manner as before. Note that these tweets were not used for training the classifier reported in the paper (classifier model given in the [/classifier directory](/classifier))


- `Cotfas et.al.` provided a set of tweets on COVID-19 vaccines in their paper titled "The Longest Month: Analyzing COVID-19 Vaccination Opinions Dynamics from Tweets in the Month following the First Vaccine Announcement". 
They have provided the tweet IDs along with their corresponding labels in their [Github repository](https://github.com/liviucotfas/covid-19-vaccination-hesitancy "Cotfas Github repository").
We collected the tweet objects in April 2021, and provided the tweet texts in [cotfas_data.csv](cotfas_data.csv). Some tweets had been deleted by the time we tried to collect them, and thus could not be fetched.



For all of these datasets, the usernames from the tweet texts have been removed to preserve their anonymity.



## Citation
If you use either of these datasets, please cite the corresponding papers as given in the [main README](/README.md) in the root directory.
