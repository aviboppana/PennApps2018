from stylistic_processing import *
import mongo_connect as mc
import table
import pandas as pd
import pickle

class news:
	def __init__(self, truth, body, body_tag_dict, body_word_count, body_avg_word_length, title, title_tag_dict, title_word_count, title_avg_word_length):
		self.truth = truth
		self.body = body
		self.body_tags = body_tag_dict
		self.body_word_count = body_word_count
		self.body_avg_word_len = body_avg_word_length
		self.title = title
		self.title_tags = title_tag_dict
		self.title_word_count = title_word_count
		self.title_avg_word_len = title_avg_word_length


def get_from_pickle(filename):
	try:
		with open(filename, 'rb') as pickle_file:
			return pickle.load(pickle_file)
	except FileNotFoundError:
		return None

def save_to_pickle(data, filename):
	with open(filename, 'wb+') as pickle_file:
		pickle.dump(data, pickle_file)

def find_max_tags(key, table):
	text_tags = table[key]
	max_len = 0
	index = -1
	
	for i in range(len(text_tags)):

		if len(text_tags[i]) > max_len:
			index = i
			max_len = len(text_tags[i])
	
	return text_tags[index].keys()

def analyze_news():
	baseTable = table.getTable(1000)
	text_tags = []
	title_tags = []
	text_word_count = []
	text_avg_word_length = []
	title_word_count = []
	title_avg_word_length = []
	
	for item in baseTable.iterrows():
		title = item[1][0]
		
		title_tag = get_tag_count(title)
		title_tags.append(title_tag)
		#print(title)
		word_count, word_length = word_count_length(title)
		title_avg_word_length.append(word_length)
		title_word_count.append(word_count)
	
	
	for item in baseTable.iterrows():
		text = item[1][1]
		
		text_tag = get_tag_count(text)

		text_tags.append(text_tag)
		word_count, word_length = word_count_length(text)
		text_avg_word_length.append(word_length)
		text_word_count.append(word_count)
		
	title_word_count = pd.Series(title_word_count, name = 'titlewc')
	title_avg_word_length = pd.Series(title_avg_word_length, name = 'titleLength')
	title_tags = pd.Series(title_tags, name = 'titleTags')
	text_tags = pd.Series(text_tags, name = 'textTags')
	text_word_count = pd.Series(text_word_count, name = 'textwc')
	text_avg_word_length = pd.Series(text_avg_word_length, name = 'textLength')
	
	
	newsTable = pd.concat([baseTable, title_tags, title_word_count, title_avg_word_length , text_tags, text_word_count, text_avg_word_length], axis = 1) 
		
	return newsTable, baseTable

def final_table(news_table, base_table, maxtitle, maxtext):
	df_title = pd.DataFrame(columns = maxtitle)
	df_text = pd.DataFrame(columns = maxtext)
	
	for dict in news_table['titleTags']:
		#for each dict add a new row to pandas dataframe
		values = []
		for key in maxtitle:
			if key not in dict:
				values.append(0)
			else:
				values.append(dict[key])
		valuesSeries = pd.Series(values, index = maxtitle)
		df_title = df_title.append(valuesSeries, ignore_index=True)
	
	for dict in news_table['textTags']:
		#for each dict add a new row to pandas dataframe
		values = []
		for key in maxtext:
			if key not in dict:
				values.append(0)
			else:
				values.append(dict[key])
		valuesSeries = pd.Series(values, index = maxtext)
		df_text = df_text.append(valuesSeries, ignore_index=True)
			
		
	return pd.concat([base_table, df_title, df_text], axis = 1)
		
			
			

def export_to_csv(real_news, fake_news, max_text_tag, max_):
	csv = open("stylistic_features.csv", "w+")
	
	sample_news = real_news[0]
	
	csv.write("truth"+",")
	csv.write("text"+',')
	csv.write("title"+',')
	csv.write("body_word-count"+',')
	csv.write("body_avg_word_len"+',')
	csv.write("title_word_count"+',')
	csv.write("title_avg_word_len"+',')
	
	sample_body_tag = real_news[0].body_tags
	#be careful assumuing the fist one is correct
	body_keys = sorted(sample_body_tag.keys())
	title_keys = sorted(real_news[0].title_tags)
	
		
	csv.close()

if __name__ == '__main__':
	news_table, base_table = analyze_news()
	#max_title_tags = list(find_max_tags("titleTags", table))
	#max_text_tags = list(find_max_tags("textTags", table))
	#save_to_pickle(max_title_tags, "max_title.pickle")
	#save_to_pickle(max_text_tags, "max_text.pickle")
	max_title_tags = get_from_pickle("max_title.pickle")
	max_text_tags = get_from_pickle("max_text.pickle")
	final = final_table(news_table, base_table, max_title_tags, max_text_tags)
	
	final.to_csv("Final_Table.csv")
	
	