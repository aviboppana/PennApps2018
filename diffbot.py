import urllib.parse
import urllib.request
import json
import ast

def get_token():
	with open("token.txt",'r') as f:
		return f.read()

def retrieve_from_url(url, token):
	'''
	Retrieves json of text title etc from diffbot api
	'''
	
	diffbot_url = "https://api.diffbot.com/v3/article"
	parameters = urllib.parse.urlencode({"url": url, "token": token})
	get_request = diffbot_url + "?" + parameters
	content = urllib.request.urlopen(get_request).read()
	
	return content

if __name__ == '__main__':
	url = "https://www.npr.org/2018/09/07/645637404/dallas-police-officer-kills-man-in-his-apartment-says-she-thought-it-was-her-hom"
	r = retrieve_from_url(url, get_token())
	
	result = r.decode("utf-8")
	result = json.loads(result)
	
	print(result['objects'][0]["text"])
