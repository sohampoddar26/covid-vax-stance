# COVID-19 vaccine Datasets

## Introduction
This directory contains datasets of tweets labelled into three classes according to their stance towards COVID-19 vaccines:- 
- **AntiVax:** the tweet is against the use of vaccines
- **ProVax:** the tweet is supporting the use of vaccines
- **Neutral:** Neither of the above


## Dataset Description
We have provided the tweet IDs, anonymized tweet texts and the corresponding labels in standard CSV files. These can be read using any standard CSV reading tool, e.g. in Python, either of the "csv" or "pandas" libraries can be used.

[Our collected dataset](our_data.csv) consists of tweets on COVID-19 vaccines between March to December of 2020. Each tweet was labelled by 3 annotators on the crowdsourcing platform [Prolific](https://prolific.co "Prolific"). 
For more details on the data collection and annotation process please read our paper on [Arxiv](https://arxiv.org "Paper on Arxiv").

`Cotfas et.al.` provided a set of tweets on COVID-19 vaccines from between November to December of 2020 in their paper titled "The Longest Month: Analyzing COVID-19 Vaccination Opinions Dynamics from Tweets in the Month following the First Vaccine Announcement". 
They have provided the tweet IDs along with their corresponding labels on [Github](https://github.com/liviucotfas/covid-19-vaccination-hesitancy "Cotfas Github repository").
We collected the tweet objects in April 2021, and provided the tweet texts in [cotfas_data.csv](cotfas_data.csv). Some tweets had been deleted by the time we tried to collect them, and thus could not be fetched.


For both the datasets, the usernames from the tweet texts have been removed to preserve their anonymity.


## Citation
If you use either of these datasets, please cite the corresponding papers as given in the [main README](/README.md) in the root directory.
