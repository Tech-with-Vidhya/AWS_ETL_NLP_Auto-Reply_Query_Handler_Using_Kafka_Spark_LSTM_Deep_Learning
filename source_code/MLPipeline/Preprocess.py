
import re
from nltk import PorterStemmer
import string
from sklearn.model_selection import train_test_split
import pandas as pd
import nltk

from .References import References

class Preprocessing(References):

    def __init__(self):
        nltk.download('stopwords')


    def clean_text(self, txt):
        """
        removing all hashtags , punctuations, stop_words  and links, also stemming words
        """
        from nltk.corpus import stopwords
        txt = txt.lower()
        txt = re.sub(r"(?<=\w)nt", "not", txt)  # change don't to do not cna't to cannot
        txt = re.sub(r"(@\S+)", "", txt)  # remove hashtags
        txt = re.sub(r'\W', ' ', str(txt))  # remove all special characters including apastrophie
        txt = txt.translate(str.maketrans('', '', string.punctuation))  # remove punctuations
        txt = re.sub(r'\s+[a-zA-Z]\s+', ' ', txt)  # remove all single characters (it's -> it s then we need to remove s)
        txt = re.sub(r'\s+', ' ', txt, flags=re.I)  # Substituting multiple spaces with single space
        txt = re.sub(r"(http\S+|http)", "", txt)  # remove links
        txt = ' '.join([PorterStemmer().stem(word=word) for word in txt.split(" ") if
                        word not in stopwords.words('english')])  # stem & remove stop words
        txt = ''.join([i for i in txt if not i.isdigit()]).strip()  # remove digits ()
        return txt

    def clean_text_NER(self, txt):
        """
        removing all hashtags , punctuations, stop_words  and links, also stemming words
        """
        txt = " ".join([self.camel_case_split(t) for t in txt.split(" ")])
        txt = re.sub(r"(?<=\w)nt", "not", txt)  # change don't to do not cna't to cannot
        txt = re.sub(r'\W', ' ', str(txt))  # remove all special characters including apastrophie
        txt = txt.translate(str.maketrans('', '', string.punctuation))  # remove punctuations
        txt = re.sub(r'\s+[a-zA-Z]\s+', ' ', txt)  # remove all single characters (it's -> it s then we need to remove s)
        txt = re.sub(r'\s+', ' ', txt, flags=re.I)  # Substituting multiple spaces with single space
        txt = re.sub(r"(http\S+|http)", "", txt)  # remove links
        return txt

    def camel_case_split(self, str):
        if len(str) > 0:
            words = [[str[0]]]

            for c in str[1:]:
                if words[-1][-1].islower() and c.isupper():
                    words.append(list(c))
                else:
                    words[-1].append(c)

            return " ".join([''.join(word) for word in words])
        else:
            return ""

    def split_data_binary(self, data, X):
        """Split the dataset into train /test"""
        Y = pd.get_dummies(data['airline_sentiment']).values
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=42)
        return X_train, X_test, Y_train, Y_test


    def split_data_multiclass(self, df, X):
        """Split the dataset into train /test"""

        # Converting categorical labels to numbers.
        Y = pd.get_dummies(df['topic_desc']).values
        print('Shape of label tensor:', Y.shape)

        # Train-Test Split
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=42)
        return X_train, X_test, Y_train, Y_test

