from flask import Flask
from flask import request
from flask import jsonify
import torch
import torch.nn as nn
import torch.nn.functional as F
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


# model class definition
class NNModel(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(NNModel, self).__init__()
        self.l1 = nn.Linear(n_input, n_hidden)
        self.l2 = nn.Linear(n_hidden, n_output)
    
    def forward(self, x):
        x = F.relu(self.l1(x))
        y = self.l2(x)
        return y


# define parameters
n_input = 4
n_hidden = 20
n_output = 3

# load model
model = NNModel(n_input, n_hidden, n_output)
model.load_state_dict(torch.load('model/model.pth'))


@app.route("/predict", methods=['POST'])
def search():
    data = request.get_json()
    x = torch.Tensor([data['x']])
    y_pred = model(x)
    result = torch.max(y_pred, 1)
    pred_label = result[1].item()
    return jsonify({"label": pred_label})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=False)