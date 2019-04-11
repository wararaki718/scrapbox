import sys


def test(a, *args, b=None, **kwargs):
    print(f'a       : {a}')
    print(f'*args   : {args}')
    print(f'b       : {b}')
    print(f'**kwargs: {kwargs}')
    print('')


def main():
    test(1, 2, b=3, c=4)
    test('a', 'c', 'd', e='e', f='f')

    return 0


if __name__ == '__main__':
    sys.exit(main())
