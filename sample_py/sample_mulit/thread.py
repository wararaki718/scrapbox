import functools
import threading
import time
import sys


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
    # define threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=func, name=f'thread-{i}', args=([i]))
        threads.append(thread)
    
    # start threads
    for thread in threads:
        thread.start()

    # wait until finished
    for thread in threads:
        thread.join()
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
