import json
import sys
import requests
from sklearn.datasets import load_boston

def main():
    target_url = "http://localhost:1234/invocations"
    boston = load_boston()

    data = [boston.data[0].tolist()]
    headers = {'Content-Type': 'application/json'}
    response = requests.post(target_url, json=data, headers=headers)
    print(response.json())

    return 0

if __name__ == "__main__":
    sys.exit(main())
