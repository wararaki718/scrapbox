import importlib
import sys


def main():
    hello = importlib.import_module('pkg.hello')
    print(hello.get_hello_world())

    return 0


if __name__ == '__main__':
    sys.exit(main())
