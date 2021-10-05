import sys
import string
import csv
from collections import OrderedDict

def preprocess(csv_file):
    pass

def add_words(text, word_dict_empty):
    """
    This function strips out the punctuations within an article, and add
    words to the provided ORDERED dictionary if they are not already in there. 
    The values of the dictionary is ignored.
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    for word in text.split(' '):
        word_dict_empty[word] = 0

def count_words(text, word_dict_empty):
    """
    This function counts the words in an article and returns a list of values 
    corresponding to the counts of word appeared in the article.
    """
    word_dict = word_dict_empty.copy()
    text = string.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    for word in text.split(' '):
        word_dict[word] = word_dict[word] + 1
    return list(word_dict.values())

def main():
    word_dict_empty = OrderedDict()

    with open('train.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(', '.join(row))

if __name__ == "__main__":
    main()