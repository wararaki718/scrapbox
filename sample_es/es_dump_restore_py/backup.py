import sys

# from elasticsearch.client import SnapshotClient
from elasticsearch import Elasticsearch


def create_es_repository(client, repository_name, location_path):
    client.create_repository(
        repository=repository_name,
        body={
            "type": "fs",
            "settings": {
                "location": location_path
            }
        }
    )
    repositories = client.get_repository(
        repository=repository_name
    )
    return repositories


def create_es_snapshots(client, repository_name, snapshot_name):
    client.create(
        repository=repository_name,
        snapshot=snapshot_name,
        wait_for_completion=True
    )
    snapshots = client.get(
        repository=repository_name,
        snapshot=snapshot_name
    )
    return snapshots


def main():
    es_host = 'http://localhost:9200'
    es_client = Elasticsearch(hosts=[es_host])

    repository_name = 'my_backup'
    location_path = '/var/lib/elasticsearch/snapshots'
    snapshot_name = 'snapshot_1'

    # create repository
    repos = create_es_repository(es_client.snapshot, repository_name, location_path)
    print(repos)

    # create snapshot
    snaps = create_es_snapshots(es_client.snapshot, repository_name, snapshot_name)
    print(snaps)

    print('DONE.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
