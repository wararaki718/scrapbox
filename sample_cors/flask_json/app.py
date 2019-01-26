from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/msg", methods=['POST'])
def search():
    data = request.get_json()
    print(data)
    return data["msg"]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5556, debug=False)
