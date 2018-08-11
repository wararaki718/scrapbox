#!/bin/bash

docker pull jupyter/pyspark-notebook

CURRENT_PATH=`pwd`

echo "download sample datasets"
wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip -O ${CURRENT_PATH}/work/ml-latest-small.zip
unzip ${CURRENT_PATH}/work/ml-latest-small.zip -d work
rm ${CURRENT_PATH}/work/ml-latest-small.zip

echo "run docker container"
docker run -p 8888:8888 -v ${CURRENT_PATH}/work:/home/jovyan/work -t jupyter/pyspark-notebook

echo "browse http://127.0.0.1:8888"
