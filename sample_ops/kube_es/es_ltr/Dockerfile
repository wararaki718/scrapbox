FROM docker.elastic.co/elasticsearch/elasticsearch:6.5.2

RUN bin/elasticsearch-plugin install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.1.0-es6.5.2.zip
RUN bin/elasticsearch-plugin install analysis-kuromoji
