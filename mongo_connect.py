import pymong
import json
import config


# takes a list of python dicts or a json objects and inserts it into mthe MLab MongoDB
def put_db(texts):
    connection = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
    db = connection[config.DB_NAME]

    db.authenticate(config.DB_USER, config.DB_PASS)

    db.insert_many(texts)
