import sys

from elasticsearch import Elasticsearch


def is_existed_index(client, es_index):
    return client.exists(es_index)


def delete_es_index(client, es_index):
    client.delete(es_index)


def restore_es_index(client, repository_name, snapshot_name):
    client.restore(
        repository=repository_name,
        snapshot=snapshot_name,
        wait_for_completion=True
    )


def main():
    es_host = 'http://localhost:9200'
    es_index = 'shakespeare'
    es_client = Elasticsearch(hosts=[es_host])

    repository_name = 'my_backup'
    snapshot_name = 'snapshot_1'

    # delete existed indices
    delete_es_index(es_client.indices, es_index)
    print(f'Is "{es_index}" exists?: {is_existed_index(es_client.indices, es_index)}')

    # restore snapshot
    restore_es_index(es_client.snapshot, repository_name, snapshot_name)
    print(f'Is "{es_index}" exists?: {is_existed_index(es_client.indices, es_index)}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
