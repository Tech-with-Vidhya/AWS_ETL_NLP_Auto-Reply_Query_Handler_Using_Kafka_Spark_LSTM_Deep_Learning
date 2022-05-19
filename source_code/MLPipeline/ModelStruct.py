
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.callbacks import EarlyStopping

import random
from spacy.util import minibatch, compounding
from pathlib import Path


import pickle
from tqdm import tqdm

from .References import References

class ModelStruct(References):

    def model_arch_binary(self, input_len):
        """Setting up the model Architecture"""

        embed_dim = 128
        lstm_out = 196
        model = Sequential()
        model.add(Embedding(self.MAX_FEATURES_BINARY, embed_dim, input_length=input_len))
        model.add(SpatialDropout1D(0.4))
        model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(2, activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model

    def model_arch_multiclass(self, input_len):
        """Setting up the model Architecture"""
        # Model Structuring
        model = Sequential()
        model.add(Embedding(self.MAX_NB_WORDS, self.EMBEDDING_DIM, input_length=input_len))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(8, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model

    def train_mode_binaryl(self, model, X_train, Y_train):
        """Training Binary Classifier Model"""

        batch_size = 32
        tqdm(model.fit(X_train, Y_train, epochs=7, batch_size=batch_size, verbose=2))
        return model

    def train_model_multiclass(self, model, X_train, Y_train):
        """Training Binary Classifier Model"""

        epochs = 10
        batch_size = 64
        early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=1, mode='auto')

        history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1,
                            callbacks=[early_stopping])

        return model

    def save_model_binary(self, model, tokenizer):
        """ saving trained model"""

        model.save(self.ROOT_DIR+self.OUTPUT + "binaryClassificationModel.h5")

        # saving tokenizer
        with open(self.ROOT_DIR +self.OUTPUT + 'tokenizerBinaryClassification.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def save_model_multiclass(self, model, tokenizer):
        """ saving trained model"""

        # saving model
        model.save_weights(self.ROOT_DIR+self.OUTPUT + "model_multiclass/multiclassComplaintClassifier.h5")

        # saving tokenizer
        with open(self.ROOT_DIR+self.OUTPUT + 'model_multiclass/tokenizerMulticlassComplaintClassification.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)



    def train_NER(self, nlp, unaffected_pipes):
        """TRAINING THE MODEL"""

        with nlp.disable_pipes(*unaffected_pipes):

            # Training for 30 iterations
            for iteration in range(30):

                # shuufling examples  before every iteration
                random.shuffle(self.TRAIN_DATA)
                losses = {}
                # batch up the examples using spaCy's minibatch
                batches = minibatch(self.TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
                for batch in batches:
                    texts, annotations = zip(*batch)
                    nlp.update(
                        texts,  # batch of texts
                        annotations,  # batch of annotations
                        drop=0.5,  # dropout - make it harder to memorise data
                        losses=losses,
                    )
                    print("Losses", losses)

            return nlp

    def save_NER(self, nlp):
        """ Save the  model to directory """

        output_dir = Path(self.ROOT_DIR +self.OUTPUT+ 'model_NER/')
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

