#!/bin/bash
echo "build image."
docker build -t hello .

echo ""
echo "run container"
docker run -it --rm hello