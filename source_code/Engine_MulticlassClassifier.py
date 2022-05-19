

# importing required libraries
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from MLPipeline.References import References
from MLPipeline.Preprocess import Preprocessing
from MLPipeline.WordEmbedding import WordEmbedding
from MLPipeline.ModelStruct import ModelStruct
from MLPipeline.Evaluate import EvaluateModel
from MLPipeline.MulticlassComplainInference import MulticlassComplainInference

class Training_MulticlassClassifier(References):

    def __init__(self):
        self.preprocess = Preprocessing()
        self.load_data()
        self.embedding = WordEmbedding()
        self.model_struct = ModelStruct()
        self.evaluate = EvaluateModel()


    def load_data(self):
        """Load dataset"""

        # Reading Dataset
        self.data = pd.read_csv(self.ROOT_DIR+self.INPUT+ 'dataset/labelled_airline_tweet.csv')

        # Keeping only the neccessary columns
        self.data = self.data[['topic_desc', 'text']]

        # Data Cleaning
        self.data['text'] = self.data['text'].apply(self.preprocess.clean_text)


    def train(self):
        """ Train Multiclass Model """
        # Loading the Dataset
        self.load_data()

        # Embedding Text
        X, tokenizer = self.embedding.word_embedding_multiclass(self.data)

        # Setting up model architecture
        self.model = self.model_struct.model_arch_multiclass(X.shape[1])

        # Splitting the Dataset
        X_train, X_test, Y_train, Y_test = self.preprocess.split_data_multiclass(self.data, X)

        # Training the model
        self.model = self.model_struct.train_model_multiclass(self.model, X_train, Y_train)

        # Saving the model
        self.model_struct.save_model_binary(self.model, tokenizer)

        # Evaluating the model
        X_validate, Y_validate = self.evaluate.evaluate_model(X_test, Y_test)
        self.evaluate.class_based_accuracy(X_validate, Y_validate, X_test, self.model)





"""Trining Starts"""
t = Training_MulticlassClassifier()
t.train()
"""Trining Ends"""


"""Inferencing Starts"""
# i = MulticlassComplainInference()
# text = input()
# i.predict_complaint_type(text)
"""Inferencing Starts"""








