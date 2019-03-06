'''
refs:
https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html
'''

import sys

from sklearn import datasets
from sklearn.utils import resample


def main():
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target

    # holdout
    x_samples, y_samples = resample(data, target, n_samples=50)

    print('data')
    print(x_samples[:5])

    print('target')
    print(y_samples[:5])

    return 0


if __name__ == '__main__':
    sys.exit(main())
