#!/bin/bash

# check elasticsearch directory
if [ ! -d 'elasticsearch-6.7.1' ]; then
    ### setup java
    export JAVA_HOME=/usr/lib/jvm/java-8-oracle
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
    sudo apt-get update
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install -y oracle-java8-installer curl

    # setup elasticsearch
    ### download elasticsearch
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.7.1.tar.gz
    tar xvzf elasticsearch-6.7.1.tar.gz
    rm elasticsearch-6.7.1.tar.gz

    ### setup plugins
    ./elasticsearch-6.7.1/bin/elasticsearch-plugin install analysis-kuromoji
    echo "[DONE] elasticsearch setup"
fi

### run
./elasticsearch-6.7.1/bin/elasticsearch
