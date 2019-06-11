import sys

import numpy
import scipy


def main():
    print('numpy config (anaconda:2019.03 image):')
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
