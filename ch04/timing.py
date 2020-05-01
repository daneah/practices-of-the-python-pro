# Using timeit to measure code execution time
from timeit import timeit

setup = 'from datetime import datetime'  # <1>
statement = 'datetime.now()'  # <2>
result = timeit(setup=setup, stmt=statement, number=1_000)  # <3>
print(f'Took an average of {result / 1_000}s, or {result}ms')


# Functions that need to be profiled to compare their performance
import random


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()


def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()


if __name__ == '__main__':
    sort_expensive()
    for i in range(1000):
        sort_cheap()
