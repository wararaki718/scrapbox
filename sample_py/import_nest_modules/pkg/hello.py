'''
nested base module
'''
import os
import sys

sys.path.append(os.path.dirname(__file__)) # import で参照するディレクトリを追加する。
import module


def get_hello_world():
    return f'hello, {module.get_world()}!'


if __name__ == '__main__':
    print(get_hello_world())
