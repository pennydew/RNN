from nltk import word_tokenize, pos_tag
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords

import pandas as pd




lem = WordNetLemmatizer()
tokenizer=TweetTokenizer()

data_train = pd.read_csv("resources/train.csv", low_memory=False)
data_test = pd.read_csv("resources/test.csv", low_memory=False)

merge = pd.concat([data_train, data_test])
df = merge.reset_index(drop=True)

merge["comment_text"]=merge["comment_text"].fillna("_na_").values
