#!/bin/bash

CONTAINER_ID=`docker container ls -a | awk '!/(CONTAINER ID)/ {print $1}'`
docker stop ${CONTAINER_ID}
docker rm ${CONTAINER_ID}

echo "DONE"
