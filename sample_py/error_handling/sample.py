import traceback
import sys

def test(a, b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print('error:', e)
        print(traceback.format_exc())


def main():
    result = test(1, 0)
    print(result)
    result = test('a', 1)
    print(result)
    return 0


if __name__ == '__main__':
    sys.exit(main())
