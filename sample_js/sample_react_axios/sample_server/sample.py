from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/msg', methods=['GET'])
def message():
    response = jsonify({
        'message': 'hello',
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    })
    return response

if __name__ == '__main__':
    app.run(port=5555)