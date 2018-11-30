"""
bulk
"""
import ast
import sys
import json
from elasticsearch import Elasticsearch


def main():
    es_host = 'localhost:9200'
    es_index = 'kamen'
    es_type = 'rider'
    es_client = Elasticsearch(hosts=[es_host])

    bulks  = []
    with open('jsons/data.json', 'r') as f:
        for line in f:
            bulks.append(ast.literal_eval(line))
    
    es_client.bulk(index=es_index, doc_type=es_type, body=bulks)
    print("DONE")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
