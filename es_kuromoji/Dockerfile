FROM elasticsearch:6.5.1

RUN elasticsearch-plugin  install analysis-kuromoji

RUN curl -XPUT localhost:9200/kamen -d @index.json

RUN curl -XPOST -H "Content-Type: application/x-ndjson" localhost:9200/_bulk -d @data.ndjson