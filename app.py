from flask import Flask, request
import pymongo
from model import *
import config
from diffbot import *
from sklearn.pipeline import Pipeline


app = Flask(__name__)
conn = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
db = conn[config.DB_NAME]
db.authenticate(config.DB_USER, config.DB_PASS)

model = train_model(db)


@app.route('/get_pred', methods=['GET'])
def get_pred():
    url = request.form['url']
    data = retrieve_from_url(url, config.api_token)

    if not data:
        return 'URL does not refer to article', 200

    return pipe.predict(data['text'])
