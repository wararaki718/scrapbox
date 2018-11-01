#!/bin/bash
CURRENT_PATH=`pwd`
wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip -O ${CURRENT_PATH}/ml-latest-small.zip
unzip ${CURRENT_PATH}/ml-latest-small.zip -d .
rm ${CURRENT_PATH}/ml-latest-small.zip