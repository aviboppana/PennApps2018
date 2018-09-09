from analyze_statistics import get_from_pickle

def load_model():
	model = get_from_pickle("xboost.pickle")
	return model

def assess(url, model):
	data = retrieve_from_url(url, config.token)
	try:
		if not data:
        	return 'Not a valid article'
        if model.predict([data])[0]:
        	return 'Real'
        else:
        	return 'Fake'
    except:
    	return 'Not a valid article'

if __name__ == "__main__":
	model = load_model
	while(True):
		url = input("Enter URL: ")
		result = assess(url, model)
		print(result)