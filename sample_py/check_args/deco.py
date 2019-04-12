import functools
import time
import sys


def calc_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(finish - start)
        return result
    return wrapper


@calc_time
def run():
    for i in range(100000):
        _ = i


def main():
    run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
