
from nltk import pos_tag, word_tokenize
from diffbot import *

def get_tag_count(S):
	'''
	Returns the tag count for parts of speech as a dictionary
	'''
	A = pos_tag(word_tokenize(S))
	return tags_to_dict(A)

def word_count_length(S):
	'''
	Returns the total number of words and average length in string S
	'''
	A = word_tokenize(S)
	
	count = 0
	
	length = 0
	
	for potential_word in A:
		if potential_word[0].isalpha():
			count += 1
			length += len(potential_word)
	
	try:
		return count, (length/count)
	
	except ZeroDivisionError:
		return None

def tags_to_dict(A):
	'''
	Should not be called by functions outside of this file
	Takes some array A containing word tokens and returns the parts of speech tags count as a dictionary
	'''
	D = {}
	for tuple in A:
		if tuple[1] in D:
			D[tuple[1]] += 1
		else:
			D[tuple[1]] = 1
	return D
	

if __name__ == '__main__':
	token = get_token()
	url = "https://www.npr.org/2018/09/06/645240941/opinion-a-linguists-defense-of-falsehood"
	#text = retrieve_from_url(url, token)
	print("Avi ran to the moon")
	print(get_tag_count("Avi ran to the moon"))
	#print(word_count_length(text))
	