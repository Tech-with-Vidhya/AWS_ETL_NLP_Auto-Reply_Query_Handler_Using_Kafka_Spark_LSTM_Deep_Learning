
import pickle
import numpy as np
#Text Preprocessing

from .References import References
from .Preprocess import Preprocessing
from .WordEmbedding import WordEmbedding
from .ModelStruct import ModelStruct

class MulticlassComplainInference(References):

      def __init__(self):

          self.preprocess = Preprocessing()
          self.embedding = WordEmbedding()
          self.model_struct = ModelStruct()
          self.load_models()


      def load_models(self):
          """ Loading trained models"""

          with open(self.ROOT_DIR+self.OUTPUT+'model_multiclass/tokenizerMulticlassComplaintClassification.pickle', 'rb') as handle:
              self.tokenizer = pickle.load(handle)

          self.model = self.model_struct.model_arch_multiclass(self.MAX_SEQUENCE_LENGTH)
          self.model.load_weights(self.ROOT_DIR+self.OUTPUT+"model_multiclass/multiclassComplaintClassifier.h5")


      def predict_complaint_type(self, text):
          """ Predicting Complain Main"""

          # Preprocess text
          new_tweet = self.preprocess.clean_text(text)

          # vectorizing the tweet by the pre-fitted tokenizer instance
          padded = self.embedding.infer_embedding_multiclass(new_tweet, self.tokenizer)

          # Predicting
          pred = self.model.predict(padded)

          # Mapping to class
          labels = ['Reschedule and Refund', 'Baggage Issue', 'Phone and Online Booking', 'Extra Charges',
                    'Delay and Customer Service', 'Seating Preferences', 'Reservation Issue', 'Customer Experience']


          return labels[np.argmax(pred)]
