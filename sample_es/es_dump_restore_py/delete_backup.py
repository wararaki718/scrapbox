import sys

from elasticsearch import Elasticsearch


def main():
    es_host = 'http://localhost:9200'
    es_client = Elasticsearch(hosts=[es_host])

    repository_name = 'my_backup'
    snapshot_name = 'snapshot_1'

    # delete snapshot
    es_client.snapshot.delete(
        repository=repository_name,
        snapshot=snapshot_name
    )

    # delete repository
    es_client.snapshot.delete_repository(
        repository=repository_name
    )

    # show status
    print(es_client.snapshot.status())

    return 0


if __name__ == '__main__':
    sys.exit(main())
