from flask import Flask, request, abort 
import pymongo
from model import *
import config
from diffbot import *
from sklearn.pipeline import Pipeline
import json


app = Flask(__name__)
conn = pymongo.MongoClient(config.DB_HOST, config.DB_PORT)
db = conn[config.DB_NAME]
db.authenticate(config.DB_USER, config.DB_PASS)

model = train_model(db)


@app.route('/get_pred', methods=['GET', 'POST'])
def get_pred():
    url = request.form.get('url', None)
    if not url:
        abort(400)

    data = retrieve_from_url(url, config.API_TOKEN)

    if not data:
        abort(400, {'message': 'Not an article'})
    #  return pipe.predict(data['text']), 200
    #  return "Real!" if pipe.predict(data['text']) else "Fake news!"
    resp = "Real!" if model.predict([data])[0] else "Fake news!" 
    
    return app.response_class(
        response=resp,
        status=200,
        mimetype='application/json'
    ) 
    
if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=False)
