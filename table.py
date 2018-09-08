import pandas as pd 
import mongo_connect as mc

def getTable(num):

	title = []
	text = []
	truth = []


	for item in mc.getTrueNews(num):
		if len(item['title'].strip()) == 0 or len(item['text'].strip()) == 0:
			continue
		
		title.append(item['title'])
		text.append(item['text'])
		truth.append(item['truth'])

	for item in mc.getFakeNews(num):
		if len(item['title'].strip()) == 0 or len(item['text'].strip()) == 0:
			continue
		
		title.append(item['title'])
		text.append(item['text'])
		truth.append(item['truth'])

	title = pd.Series(title, name = 'title')
	text = pd.Series(text, name = 'text')
	truth = pd.Series(truth, name = 'truth')

	table = pd.concat([title, text, truth], axis = 1)

	table.to_csv('table.csv')

	return table

