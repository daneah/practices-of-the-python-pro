# Take 1
def get_number_with_highest_count(counts):  # <1>
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = {}
    for number in numbers:  # <2>
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return get_number_with_highest_count(counts)


# Using defaultdict
from collections import defaultdict  # <1>


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = defaultdict(int)  # <2>
    for number in numbers:
        counts[number] += 1  # <3>

    return get_number_with_highest_count(counts)


# Using Counter
from collections import Counter  # <1>


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = Counter(numbers)  # <2>
    return get_number_with_highest_count(counts)


# Using lambda functions
from collections import Counter


def get_number_with_highest_count(counts):
    return max(  # <1>
        counts,
        key=lambda number: counts[number]
    )


def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)
