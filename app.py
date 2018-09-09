from flask import Flask, request
from diffbot import retrieve_from_url

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route('/get_request')
def get_request():
    url = request.form['url']
    data = retrieve_from_url(url, config.token)

    if not data:
        return 'Not a valid article', 400

    return get_prediction(title=data['title'], text=data['text']), 200


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)
