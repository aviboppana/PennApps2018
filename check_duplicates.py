import pymongo
import config
import json
import mongo_connect as mc

def no_duplicates():
	'''
	Verify that the database does not have duplicate articles
	'''
	cursor = mc.getData()
	
	
	title_set = set()
	try:
		while True:
			title = cursor.next()["title"]
			if title in title_set:
				print(title)
				return False
			else:
				title_set.add(title)
			
	except StopIteration:
		return True

def get_duplicates():
	'''
	returns array of duplicate articles titles in the database
	'''
	cursor = mc.getData()
	title_set = set()
	
	duplicates = []
	try:
		while True:
			title = cursor.next()["title"]
			if title in title_set:
				duplicates.append(title)
			else:
				title_set.add(title)
			
	except StopIteration:
		return duplicates
		
def count_duplicates_by_truthiness():
	'''
	Counts the number of duplicate articles in the database
	'''
	cursor = mc.getData()
	title_set = set()
	
	true_duplicate_count = 0
	false_duplicate_count = 0
	try:
		while True:
			article = cursor.next()
			title = article["title"]
			truth = article["truth"]
			if title in title_set:
				if truth:
					true_duplicate_count += 1
				else:
					false_duplicate_count += 1
			else:
				title_set.add(title)
			
	except StopIteration:
		return true_duplicate_count, false_duplicate_count

def count_articles():
	cursor = mc.getData()
	count = 0
	
	try:
		while True:
			cursor.next()
			count+=1
	except StopIteration:
		return count

def remove_duplicates(A):
	'''
	Removes all duplicate titles in array A from the database
	
	e.g. 
	A = [Cat, Cat]
	db = [Cat, Dog, Cat, Cat] -> [Cat, Dog]
	'''
	Collection = mc.getCollection()
	
	for article_title in A:
		Collection.delete_one({"title":article_title})

def count_true_and_false():
	'''
	Counts number of true and false articles in db
	'''
	cursor = mc.getData()
	
	trueCount = 0
	falseCount = 0
	try:
		while True:
			article = cursor.next()
			truth = article["truth"]
			if truth:
				trueCount += 1
			else:
				falseCount += 1
			
	except StopIteration:
		return trueCount, falseCount
	

if __name__ == '__main__':
	duplicates = get_duplicates()
	num_dup_true, num_dup_false = count_duplicates_by_truthiness()
	print("Duplicates by truthiness: True: {}\tFalse: {}".format(num_dup_true, num_dup_false))
	print(count_articles())
	
	num_true, num_false = count_true_and_false()
	print("Overall article truthiness: True: {}\tFalse: {}".format(num_true, num_false))
	remove_duplicates(duplicates)
	
	
	