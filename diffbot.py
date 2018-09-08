import urllib.parse
import urllib.request
import json
import ast

def get_token():
	with open("token.txt",'r') as f:
		return f.read()

def retrieve_from_url(url, token):
	'''
	Retrieves text of article using diffbot api
	'''
	
	diffbot_url = "https://api.diffbot.com/v3/article"
	parameters = urllib.parse.urlencode({"url": url, "token": token})
	get_request = diffbot_url + "?" + parameters
	content = urllib.request.urlopen(get_request).read()
	
	result = content.decode("utf-8")
	return json.loads(result)['objects'][0]["text"]

if __name__ == '__main__':
	pass