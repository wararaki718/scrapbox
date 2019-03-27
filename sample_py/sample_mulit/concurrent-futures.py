from concurrent import futures
import functools
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
def run_thread():
    # thread
    with futures.ThreadPoolExecutor() as executer:
        executers = []
        for i in range(3):
            executers.append(executer.submit(func, i))
        results = [e.result() for e in executers]
    
    return results


@calc_time
def run_process():
    # process
    with futures.ProcessPoolExecutor() as executer:
        executers = []
        for i in range(3):
            executers.append(executer.submit(func, i))
        results = [e.result() for e in executers]
    
    return results


def main():
    print('thread:')
    run_thread()

    print('process:')
    run_process()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
