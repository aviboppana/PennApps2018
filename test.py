import config, json
from mongo_connect import put_db


test_case = {'title': 'test title', 'text': 'test text', 'real': False}
put_db([test_case])

