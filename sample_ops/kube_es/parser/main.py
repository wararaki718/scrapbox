import logging
import sys


def init_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s :%(message)s'
    )
    return logging.getLogger(__name__)


def main():
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
