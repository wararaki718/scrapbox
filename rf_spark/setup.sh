#!/bin/bash

docker pull jupyter/pyspark-notebook

CURRENT_PATH=`pwd`

echo "run docker container"
docker run -p 8888:8888 -v ${CURRENT_PATH}/work:/home/jovyan/work -t jupyter/pyspark-notebook

echo "browse http://127.0.0.1:8888"
