# Take 1
names = ['Larry', 'Curly', 'Moe']
message = 'The Three Stooges: '
for index, name in enumerate(names):
    if index > 0:
        message += ', '
    if index == len(names) - 1:
        message += 'and '
    message += name
print(message)


# Repetition
names = ['Moe', 'Larry', 'Shemp']
message = 'The Three Stooges: '
for index, name in enumerate(names):
    if index > 0:
        message += ', '
    if index == len(names) - 1:
        message += 'and '
    message += name
print(message)

names = ['Larry', 'Curly', 'Moe']
message = 'The Three Stooges: '
for index, name in enumerate(names):
    if index > 0:
        message += ', '
    if index == len(names) - 1:
        message += 'and '
    message += name
print(message)


# Extract function
def introduce_stooges(names):  # <1>
    message = 'The Three Stooges: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'and '
        message += name
    print(message)


introduce_stooges(['Moe', 'Larry', 'Shemp'])  # <2>
introduce_stooges(['Larry', 'Curly', 'Moe'])


# Generalize function
def introduce(title, names):  # <1>
    message = f'{title}: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'and '
        message += name
    print(message)


introduce('The Three Stooges', ['Moe', 'Larry', 'Shemp'])  # <2>
introduce('The Three Stooges', ['Larry', 'Curly', 'Moe'])

introduce(  # <3>
    'Teenage Mutant Ninja Turtles',
    ['Donatello', 'Raphael', 'Michaelangelo', 'Leonardo']
)

introduce('The Chipmunks', ['Alvin', 'Simon', 'Theodore'])


# Extract further to separate concerns
def join_names(names):  # <1>
    name_string = ''

    for index, name in enumerate(names):
        if index > 0:
            name_string += ', '
        if index == len(names) - 1:
            name_string += 'and '
        name_string += name
    return name_string


def introduce(title, names):  # <2>
    print(f'{title}: {join_names(names)}')