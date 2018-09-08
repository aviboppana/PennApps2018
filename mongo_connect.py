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


def getData():
	connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
	db = connection[config.DB_NAME]

	db.authenticate(config.DB_USER, config.DB_PASS)

	return db.docs.find()
