import sys

from mods.mod import sub
from mods.mod2 import sub2


def main():
    print('start')
    print(sub.sub_func())
    print(sub2.sub2_func())

    # not call
    print(sub.sub_func2())
    return 0


if __name__ == '__main__':
    sys.exit(main())
