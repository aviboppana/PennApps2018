import pymongo
import json
import config


# takes a list of json objects and inserts it into mthe MLab MongoDB
def put_db(texts):
    connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
    db = connection[config.DB_NAME]

    db.authenticate(config.DB_USER, config.DB_PASS)

    for text in texts:
        db.docs.insert(text)

def getCollection():
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	return db.docs

def getData():
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	return db.docs.find()

def getTrueNews(num):
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	return db.docs.find({'truth': True}).limit(num)

def getFakeNews(num):
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	return db.docs.find({'truth': False}).limit(num)

def doesExist(title):
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	if db.docs.find({'title': title}).count() > 0:
		return True
	else:
		return False