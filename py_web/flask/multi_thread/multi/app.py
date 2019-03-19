import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    start = time.time()
    time.sleep(5)
    finish = time.time() - start
    return f'api: {finish}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5556, debug=False, threaded=True)
