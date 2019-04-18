import sys

from mod import sub
from mod2 import sub2


def main():
    print('start')
    print(sub.sub_func())
    print(sub2.sub2_func())

    # not call
    # print(sub.sub_main_func())
    return 0


if __name__ == '__main__':
    sys.exit(main())
