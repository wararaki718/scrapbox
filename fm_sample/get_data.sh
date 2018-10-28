#!/bin/bash
# download data.
# wget http://s3-eu-west-1.amazonaws.com/yc-rdata/yoochoose-dataFull.7z

wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip

# brew install p7zip
# 7z x yoochoose-dataFull.7z
unzip ml-latest-small.zip

echo "Done"