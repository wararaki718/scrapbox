import functools
import sys
import time

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'time : {end-start}')
        return result
    return wrapper


@decorator
def fit(model, X, y):
    return model.fit(X, y)


def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    model = RandomForestClassifier()
    model = fit(model, X_train, y_train)

    score = model.score(X_test, y_test)
    print(f'score: {score}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
