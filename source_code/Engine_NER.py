

#Named Entity Recognition
import en_core_web_sm

from MLPipeline.References import References
from MLPipeline.ModelStruct import ModelStruct
from MLPipeline.NameEntityInference import NameEntitiesInference

class Train_NER(References):

    def __init__(self):
        self.model_struct = ModelStruct()
        self.nlp = en_core_web_sm.load()

        # Disable pipeline components you dont need to change
        self.unaffected_pipes = [pipe for pipe in self.nlp.pipe_names if pipe not in self.PIPE_EXECPTIONS]


    def train_entity(self):
        self.nlp = self.model_struct.train_NER(self.nlp, self.unaffected_pipes)
        self.model_struct.save_NER(self.nlp)


"""Training Starts"""
t = Train_NER()
t.train_entity()
"""Training Ends"""


"""Inferencing Starts"""
# i = NameEntitiesInference()
# text = input()
# i.get_Entities(text)

"""Inferencing Ends"""