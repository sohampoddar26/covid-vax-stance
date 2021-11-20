# Winds of Change: Impact of COVID-19 on Vaccine-related Opinions of Twitter users

## Information
This repository contains the data and classifier used in the paper titled "Winds of Change: Impact of COVID-19 on Vaccine-related Opinions of Twitter users" accepted to appear at the [International Conference on Web and Social Media (AAAI ICWSM) 2022](https://www.icwsm.org/2022/index.html/ "ICWSM Website").

A preprint of the paper is available on [Arxiv](https://arxiv.org "Paper on  Arxiv").

There are two directories as given below. The details are given in the README files in the corresponding directories.
- [dataset](./dataset) -- consisting of a collection of tweets with crowdsourced labels of their stance towards COVID-19 vaccines.
- [classifiers](./classifiers) -- consisting of codes to run our classifier to predict the vaccine-stances of a set of tweets (or any text)


## Citation
If you use either our dataset or classifier, please cite the following paper:
```
@inproceedings{poddar2022windsofchange,
  title={Winds of Change: Impact of COVID-19 on Vaccine-related Opinions of Twitter users},
  author={Poddar, Soham and Mondal, Mainack and Misra, Janardan and Ganguly, Niloy and Ghosh, Saptarshi},
  booktitle={Proceedings of the Sixteenth International AAAI Conference on Web and Social Media (ICWSM'22)},
  year={2022}
}
```


We have also given the data provided by [Cotfas et.al.](https://github.com/liviucotfas/covid-19-vaccination-hesitancy "original repository") in the [dataset](./dataset) directory (details given in the the README inside this directory). If you use their dataset, please cite their paper:
```
@article{cotfas2021longest,
  title={The Longest Month: Analyzing COVID-19 Vaccination Opinions Dynamics from Tweets in the Month following the First Vaccine Announcement},
  author={Cotfas, Liviu-Adrian and Delcea, Camelia and Roxin, Ioan and Ioan{\u{a}}{\c{s}}, Corina and Gherai, Dana Simona and Tajariol, Federico},
  journal={IEEE Access},
  volume={9},
  pages={33203--33223},
  year={2021},
  publisher={IEEE}
}
```
