#!/bin/bash

docker pull jupyter/datascience-notebook

CURRENT_PATH=`pwd`
docker run -p 8888:8888 -v ${CURRENT_PATH}//work:/home/jovyan/work -t jupyter/datascience-notebook

echo "browse http://127.0.0.1:8888"
