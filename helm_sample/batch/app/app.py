"""
batch application
"""
import sys
from redis import Redis

redis = Redis(host='127.0.0.1', port=6379)

def main():
    print("hello, batch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
