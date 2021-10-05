import pandas as pd
import os
import re
import nltk
from nltk.tokenize import word_tokenize
from autocorrect import Speller
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('wordnet')
nltk.download('punkt')

data1 = pd.read_csv(os.getcwd() + '/Dataset/Data1_Fake.csv')

def add_words(data):
    data = re.sub('[^A-Za-z]', ' ', data)
    data = data.lower()
    tokenized_data = word_tokenize(data)

    lemma = nltk.wordnet.WordNetLemmatizer()
    for i in range(len(tokenized_data)):
        tokenized_data[i] = lemma.lemmatize(tokenized_data[i])

    spell = Speller(lang='en')
    for i in range(len(tokenized_data)):
        tokenized_data[i] = spell(tokenized_data[i])
    data_text = " ".join(tokenized_data)
    # creating the feature matrix
    return data_text

text = []

#for i in range(10):
for i in range(data1.shape[0]):
    text.append(add_words(data1.iloc[i,1]))

print(text)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text).toarray()

print(X.shape)
print(X)