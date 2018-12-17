from flask import Flask

app = Flask(__name__)

@app.route("/msg")
def search():
    return "cors prohibit"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5556, debug=False)
