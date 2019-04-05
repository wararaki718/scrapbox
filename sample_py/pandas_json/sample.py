import sys

import pandas as pd
from pandas.io.json import json_normalize


def init_data():
    data = [
        {
            "id": 1,
            "name": {
                "first": "hoge",
                "last": "huga"
            },
            "age": 10,
            "location": {
                "country": "Japan",
                "prefecture": "Tokyo",
                "city": "Shibuya"
            }
        },
        {
            "id": 2,
            "name": {
                "first": "test",
                "last": "sample"
            },
            "age": 20,
            "location": {
                "country": "Japan",
                "prefecture": "Kanagawa",
                "city": "Yokohama"
            }
        }
    ]
    return data


def main():
    data = init_data()

    df = pd.DataFrame(data)
    print(df)
    print('\n')

    df = json_normalize(data)
    print(df)

    return 0


if __name__ == '__main__':
    sys.exit(main())
