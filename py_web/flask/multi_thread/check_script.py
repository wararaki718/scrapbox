from concurrent import futures
import functools
import sys
import time

import requests


def calc_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'elapsed time: {finish-start}')
        return result 
    return wrapper


def check(i, url):
    response = requests.get(url)
    return response.text


@calc_time
def single_check():
    print('single check:')
    url = 'http://localhost:5555'

    with futures.ThreadPoolExecutor() as executer:
        executers = []
        for i in range(3):
            executers.append(executer.submit(check, i, url))
        results = [e.result() for e in executers]

    print(results)


@calc_time
def multi_check():
    print('multi check:')
    url = 'http://localhost:5556'

    with futures.ThreadPoolExecutor() as executer:
        executers = []
        for i in range(3):
            executers.append(executer.submit(check, i, url))
        results = [e.result() for e in executers]

    print(results)


def main():
    single_check()
    print('')
    multi_check()

    return 0


if __name__ == '__main__':
    sys.exit(main())
