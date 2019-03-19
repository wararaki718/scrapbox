from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def world():
    return 'flask_web2'


@app.route("/via")
def hello():
    response = requests.get('http://pynet:5555')
    return f'flask_web2 & {response.text}'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5556, debug=False)
