


import spacy
import en_core_web_sm
from pathlib import Path
from .Preprocess import Preprocessing
from .References import References

class NameEntitiesInference(References):


    def __init__(self):
        """ Initialization """

        self.preprocess = Preprocessing()
        self.nlp = en_core_web_sm.load()  # Load the saved model and predict
        output_dir = Path(self.ROOT_DIR+self.OUTPUT + 'model_NER/')
        self.nlp_updated = spacy.load(output_dir)


    def get_Entities(self, text):
        """ Getting Entites from text """

        text = self.preprocess.clean_text_NER(text)
        doc = self.nlp_updated(text)
        labels = [(X.text, X.label_) for X in doc.ents]

        doc = self.nlp(text)
        labels_norm = [(X.text, X.label_) for X in doc.ents]
        labels.extend(labels_norm)

        return labels
