import random
import time


def an_expensive_function():
    execution_time = random.random() / 100  # <1>
    time.sleep(execution_time)


if __name__ == '__main__':
    for _ in range(1000):  # <2>
        an_expensive_function()
