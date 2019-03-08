import logging
import sys
from module import hello

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def main():
    logger.info('hello')
    logger.info(hello())

    return 0


if __name__ == '__main__':
    sys.exit(main())
