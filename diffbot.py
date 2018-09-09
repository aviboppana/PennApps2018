import urllib.parse
import urllib.request
import json
import ast


def get_token():
    with open("token.txt", 'r') as f:
        return f.read()


def retrieve_from_url(url, token):
<<<<<<< HEAD
    '''
    Retrieves text of article using diffbot api
    '''

    diffbot_url = "https://api.diffbot.com/v3/article"
    parameters = urllib.parse.urlencode({"url": url, "token": token})
    get_request = diffbot_url + "?" + parameters
    content = urllib.request.urlopen(get_request).read()

    result = content.decode("utf-8")
    return json.loads(result)['objects'][0]["text"]

=======
	'''
	Retrieves text of article using diffbot api
	'''
	
	diffbot_url = "https://api.diffbot.com/v3/article"
	parameters = urllib.parse.urlencode({"url": url, "token": token})
	get_request = diffbot_url + "?" + parameters
	content = urllib.request.urlopen(get_request).read()
	
	result = content.decode("utf-8")
	try:
		return json.loads(result)['objects'][0]["text"]
	except KeyError:
		print("ERROR WITH PARSING DIFFBOT RESPONSE: ")
		print(json.loads(result))
		raise KeyError
>>>>>>> ec2b3526ae981fcf3aeee2ff4986b36ed5143b41

if __name__ == '__main__':
    pass
