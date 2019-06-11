import sys

import numpy
import scipy


def main():
    print('numpy config (miniconda:4.6.14 image):')
    print(numpy.__version__)
    print(numpy.show_config())
    print('')

    print('scipy config:')
    print(scipy.__version__)
    print(scipy.show_config())
    print('')

    return 0

if __name__ == '__main__':
    sys.exit(main())
