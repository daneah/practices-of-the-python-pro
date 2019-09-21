# How range works under the hood
def range(*args):
    if len(args) == 1: # <1>
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start

    while current < stop:
        yield current  # <2>
        current += 1  # <3>


# Creating a generator for calculating squares of numbers in a list
def squares(items):
    for item in items:
        yield item ** 2
