# Fake News Detection

We implement fake news detection in this repository. This was a COMP755: Machine Learning project done by Bongsoo Yi, Chanhwa Lee, Wanyong Feng, and Shengjie Xu. The summary of the project is as follows:

1. We implemented classical machine learning methods: naive Bayes (NB), logistic regression (LR), support vector machine (SVM), and
random forest (RF) to perform the fake news detection task. 

2. We utilized deep learning methods: deep neural network (DNN), one-dimensional convolutional neural network (1D CNN), bidirectional encoder representations from transformers (BERT), and long short-term memory (LSTM) to conduct the fake news detection with the same data settings as in the classical methods.

3. We analyzed the generalizability of the trained models by testing them on datasets that have
different distributions from the training data (e.g., testing the models trained on longer news articles to
predict the credibility of shorter, twitter styled posts). 

4. We applied transfer learning proposed by [H. Azarbonyad (2019)](https://dl.acm.org/doi/10.1145/3289600.3290984) to make a domain-independent model and compare the prediction accuracy with those of domain-dependent models (both types of models are trained on concatenated datasets).

<p align="center">
  <img src="data/overall_process.png" width="600">
  <p align = "center">
  Overall Classification process of Fake News Detection
</p>


## Data

This project used the following four datasets:

**Kaggle 1**     
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

**Kaggle 2**          
https://www.kaggle.com/ksaivenketpatro/fake-news-detection-dataset

**Kaggle 3**           
https://www.kaggle.com/jruvika/fake-news-detection?select=data.csv

**LIAR**         
https://github.com/tfs4/liar_dataset


## Preprocessing
Check `preprocessing.ipynb` for the preprocessing process.

## ML and DL Analysis
We implemented various machine learning and deep learning methods: Naive Bayes, Logistic Regression, SVM, Random Forest, Neural Network, BERT.

Check the following files:
* `NB_LR_SVM_RF.ipynb`: Naive Bayes, Logistic Regression, SVM, Random Forest
* `MLP.ipynb`: Neural Network
* `1dCNN.ipynb`: 1D CNN
* `BERT.py`: BERT


## Domain Adaptation
Check `domain_adaptation.ipynb` for domain adaptation.

<p align="center">
  <img src="data/domain_independent_model.png" width="600">
  <p align = "center">
  Structure of the domain-independent model
</p>

## Results
Check our final report `report.pdf` for the results.
