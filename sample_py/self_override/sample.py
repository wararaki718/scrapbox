import sys


class Hello:
    def __init__(self, msg='hello'):
        print(msg)
        self = World()
    
    def get_msg(self):
        print('hello')


class World:
    def __init__(self, msg='world'):
        print(msg)
    
    def get_msg(self):
        print('world')


def main():
    hello = Hello()
    hello.get_msg()
    return 0


if __name__ == '__main__':
    sys.exit(main())
