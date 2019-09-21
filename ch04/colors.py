# Loading all colors into memory at once
color_counts = {}

with open('all-favorite-colors.txt') as favorite_colors_file:
    favorite_colors = favorite_colors_file.read().splitlines()  # <1>

for color in favorite_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1


# Loading a single color at a time into memory
color_counts = {}

with open('all-favorite-colors.txt') as favorite_colors_file:
    for color in favorite_colors_file:  # <1>
        color = color.strip()  # <2>

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1


# Using a set to store only unique colors seen
all_colors = set()

with open('all-favorite-colors.txt') as favorite_colors_file:
    for line in favorite_colors_file:  # <1>
        all_colors.add(line.strip())  # <2>

print('Amber Waves of Grain' in all_colors)  # <3>
