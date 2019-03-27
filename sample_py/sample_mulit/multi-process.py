import functools
import multiprocessing
import sys
import time


def calc_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'elapsed time: {finish-start}')
        return result
    return wrapper


@calc_time
def func(n):
    print(f'start : {n}')
    for i in range(10):
        print(f'{n}: {i}')
    print(f'finish: {n}')


@calc_time
def main():
    # use pool object
    for i in range(5):
        with multiprocessing.Pool(processes=5) as pool:
            pool.map(func, ([i]))

    return 0


if __name__ == '__main__':
    sys.exit(main())
