
from .References import References
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class WordEmbedding(References):

    def word_embedding(self, data):
        """Embedding words to text sequences"""

        tokenizer = Tokenizer(num_words=self.MAX_FEATURES_BINARY, split=' ')
        tokenizer.fit_on_texts(data['text'].values)
        X = tokenizer.texts_to_sequences(data['text'].values)
        # pad: to make all input of same length
        X = pad_sequences(X)
        return X, tokenizer

    def infer_embedding(self, text, tokenizer):

        twt = tokenizer.texts_to_sequences([text])
        # padding the tweet to have exactly the same shape as `embedding_2` input
        twt = pad_sequences(twt, maxlen=28, dtype='int32', value=0)
        return twt

    def infer_embedding_multiclass(self, new_tweet, tokenizer):

        seq = tokenizer.texts_to_sequences([new_tweet])
        # padding the tweet to have exactly the same shape as `embedding_2` input
        padded = pad_sequences(seq, maxlen=self.MAX_SEQUENCE_LENGTH)

        return padded


    def word_embedding_multiclass(self, df):

        tokenizer = Tokenizer(num_words=self.MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
        tokenizer.fit_on_texts(df['text'].values)
        word_index = tokenizer.word_index
        print('Found %s unique tokens.' % len(word_index))

        # Word Embedding
        X = tokenizer.texts_to_sequences(df['text'].values)
        X = pad_sequences(X, maxlen=self.MAX_SEQUENCE_LENGTH)

        return X, tokenizer

