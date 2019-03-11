"""
dnn
"""
import json
import sys

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

from sklearn import datasets
from sklearn.model_selection import train_test_split

import tensorflow as tf


def create_model(n_input, n_output):
    model = Sequential([
        Dense(32, input_shape=(n_input,)),
        Activation('relu'),
        Dense(n_output),
        Activation('softmax')
    ])

    model.compile(
        optimizer='rmsprop',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def get_train_test_data(data, target):
    X_train, X_test, y_train, y_test = train_test_split(data, target)

    n_target = len(set(target))
    y_train = keras.utils.to_categorical(y_train, num_classes=n_target)
    y_test = keras.utils.to_categorical(y_test, num_classes=n_target)

    return (X_train, X_test, y_train, y_test)



def main():
    model_path = 'model.pkl'

    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = get_train_test_data(iris.data, iris.target)

    model = create_model(X_train.shape[1], len(set(iris.target)))
    model.fit(X_train, y_train, epochs=10, verbose=0)

    model.save(model_path)
    del model

    with tf.device("/cpu:0"):
        model = keras.models.load_model(model_path)
        loss, accuracy = model.evaluate(X_test, y_test)

    print(f'loss    : {loss}')
    print(f'accuracy: {accuracy}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
