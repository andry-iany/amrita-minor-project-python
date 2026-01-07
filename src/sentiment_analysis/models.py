import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences

from sentiment_analysis.utils import PATH_MODEL, PATH_TOKENIZER, clean_text

class SentimentAnalysisModel:
    def __init__(self):
        self.__model__ = None
        self.__tokenizer__ = None


    def initialize(self): 
        self.__internal_load_model__()
        self.__internal_load_tokenizer__()
        print("Model initialized successfully")


    def __internal_load_model__(self):
        self.__model__ = load_model(PATH_MODEL)
    
    def __internal_load_tokenizer__(self):
        with open(PATH_TOKENIZER, 'r', encoding="utf-8") as f:
            data = f.read()
            self.__tokenizer__ = tokenizer_from_json(data)
    
    
    def predict(self, texts = []):
        if (self.__model__ is None or self.__tokenizer__ is None):
            raise Exception("You need to call the initialize() method first")

        prepared_texts = self.__prepare_texts__(texts)
        predictions = self.__model__.predict(prepared_texts)
        return predictions.flatten().tolist()


    def __prepare_texts__(self, texts = []):
        prepared_texts = np.array(list(map(clean_text, texts)))

        maxlen = 250
        padding_type = 'post'

        prepared_texts = self.__tokenizer__.texts_to_sequences(prepared_texts)
        prepared_texts = pad_sequences(prepared_texts, padding=padding_type, maxlen=maxlen)
        return prepared_texts

    

