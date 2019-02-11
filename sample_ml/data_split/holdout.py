'''
refs:
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split
'''

import sys

from sklearn import datasets
from sklearn.model_selection import train_test_split


def main():
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target

    # holdout
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, shuffle=True)

    print('data')
    print(x_train[:5])
    print(x_test[:5])

    print('target')
    print(y_train[:5])
    print(y_test[:5])

    return 0


if __name__ == '__main__':
    sys.exit(main())
