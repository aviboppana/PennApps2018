from analyze_stylistics import get_from_pickle
from diffbot import *

def load_model():
    model = get_from_pickle("xboost.pickle")
    return model

def assess(url, model):
    try:
        data = retrieve_from_url(url, get_token())
        if not data:
            return 'Not a valid article'
        if model.predict([data])[0]:
            return 'Real'
        else:
            return 'Fake'
    except:
        return 'Not a valid article'

if __name__ == "__main__":
    while(True):
        model = load_model()
        url = input("Enter URL: ")
        result = assess(url, model)
        print(result)