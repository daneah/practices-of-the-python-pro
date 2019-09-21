# Python for loop
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i * i)


# Functional style
from functools import reduce

squares = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])


# List comprehension style
squares = [x * x for x in [1, 2, 3, 4, 5]]
should = all([True, True, False])
evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]


# Partial functions
from functools import partial


def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)  # <1>
cube = partial(pow, power=3)  # <2>
