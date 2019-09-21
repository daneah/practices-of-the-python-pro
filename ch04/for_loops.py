# A single for loop containing one expression
names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    print(name)


# A single for loop containing multiple expressions
names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    greeting = 'Hi, my name is'
    print(f'{greeting} {name}')


# Two for loops
names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    print(f'This is {name}!')

message = 'Let\'s welcome '
for name in names:
    message += f'{name} '
print(message)


# Nested for loops
def has_duplicates(sequence):
    for index1, item1 in enumerate(sequence):  # <1>
        for index2, item2 in enumerate(sequence):  # <2>
            if item1 == item2 and index1 != index2:  # <3>
                return True
    return False
