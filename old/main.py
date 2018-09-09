import diffbot as df
import randomnews as rn
import mongo_connect as mc
import json
import os
import threading

def main():

		truth = True

		for i in range (0, 200):
			
			article = rn.get_articles('politics', truth)
			text = df.retrieve_from_url(article[0], df.get_token())

			print(article[1])
	
			dict = {'title': article[1], 'text': text, 'truth': article[2]}

			if not mc.doesExist(article[1]):

				r = json.dumps(dict)
				loaded_r = json.loads(r)
			

				mc.put_db([loaded_r])

				print('Doc {} finished'.format(i))
				print(dict['truth'])

				truth = truth
			else:
				print('Duplicate was not added')


if __name__ == "__main__":
	main()
	
