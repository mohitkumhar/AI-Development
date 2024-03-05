import re
from bs4 import BeautifulSoup
import pickle
import numpy as np


cv = pickle.load(open('countVector.pkl', 'rb'))


def preprocessing(q):
    q = str(q).lower().strip()

    # Replace certain special characters with their string equivalents
    q = q.replace("%", 'percent')
    q = q.replace("$", 'dollor')
    q = q.replace("₹", 'rupee')
    q = q.replace("€", 'euro')
    q = q.replace("@", 'at')

    # the pattern [math] appearns around 900 times in the whole dataset
    q = q.replace('[math]', '')

    # Decontracting words
    # https://en.wikipedia.org/wiki/Wikipedia%3aList_of_English_contractions
    # https://stackoverflow.com/a/19794953
    contractions = { 
    "ain't": "am not",
    "aren't": "are not",
    "can't": "can not",
    "can't've": "can not have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
    }

    q_decontracted = []

    for word in q.split():
        if word in contractions:
            word = contractions[word]
        q_decontracted.append(word)

    q = ' '.join(q_decontracted)

    q = q.replace("'ve", " have")
    q = q.replace("'re", " are")
    q = q.replace("n't", " not")
    q = q.replace("'ll", " will")


    # remove HTML

    q = BeautifulSoup(q)
    q = q.get_text()

    # remove punctuation
    pattern = re.compile('\W')
    q = re.sub(pattern, ' ', q).strip()

    return q



def test_common_word(q1, q2):
    w1 = set(map(lambda x: x.lower().strip(), q1.split()))
    w2 = set(map(lambda x: x.lower().strip(), q2.split()))
    return len(w1 & w2)

def test_total_word(q1, q2):
    t1 = set(map(lambda x: x.lower().strip(), q1.split()))
    t2 = set(map(lambda x: x.lower().strip(), q2.split()))
    return len(t1) + len(t2)


def query_point_creator(q1, q2):
    input_query = []
    
    q1 = preprocessing(q1)
    q2 = preprocessing(q2)
    
    input_query.append(len(q1))
    input_query.append(len(q2))
    
    

    input_query.append(len(q1.split()))
    input_query.append(len(q2.split()))
    
    
    input_query.append(test_common_word(q1, q2))
    input_query.append(test_total_word(q1, q2))
    input_query.append(round(test_common_word(q1,q2) / test_total_word(q1, q2), 2))
    

    q1_bow = cv.transform([q1]).toarray()
    q2_bow = cv.transform([q2]).toarray()
    
    return np.hstack((np.array(input_query).reshape(1, 7), q1_bow, q2_bow))




    

