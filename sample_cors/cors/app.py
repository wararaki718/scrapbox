from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/msg")
def search():
    return "cors allow!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=False)
