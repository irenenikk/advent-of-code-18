import numpy as np
import math
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

from functools import reduce

def get_manhattan_distance(row1, row2, column1, column2):
    return abs(row1 - row2) + abs(column1 - column2)

def is_in_corner(coord, i, width, height):
    return i % width == 0 or i % width == 1 or math.floor(i / width) == 0 or math.floor(i / width) == (height)
    
inputs = open("test_input.txt", "r").read().splitlines()
inputs = [(int(i.split(", ")[0]), int(i.split(", ")[1]))for i in inputs]

min_row = reduce(lambda a, b: a if min(a[0], b[0]) == a[0] else b, inputs)[0]
max_row = reduce(lambda a, b: a if max(a[0], b[0]) == a[0] else b, inputs)[0]
min_col = reduce(lambda a, b: a if min(a[1], b[1]) == a[1] else b, inputs)[1] 
max_col = reduce(lambda a, b: a if max(a[1], b[1]) == a[1] else b, inputs)[1]

coordinates = []

width  = max_col - min_col +2
height = max_row - min_row +2

for row in range(0,height):
    for col in range(0, width):
        min_distance = 9999
        mini_coordinate = ''
        distances = []
        for i in inputs:
            distance = get_manhattan_distance(row, i[1], col, i[0])
            distances.append(distance)
            if distance < min_distance:
                min_distance = distance
                mini_coordinate = i
        # don't add coordinates which are the same distance from several coordinates
        duplicate_minimal_distances = list(filter(lambda x: x == min_distance, distances))
        # print(duplicate_minimal_distances)
        if len(duplicate_minimal_distances) > 1:
            coordinates.append((-1, -1))
        else:
            coordinates.append(mini_coordinate)
# define which coordinates have the closest coordinates on the sides
infinite_areas = [ coord if is_in_corner(coord, i, width, height) else None for i, coord in enumerate(coordinates)]
# filter them away
cleaned_coordinates = list(filter(lambda coord: coord not in infinite_areas, coordinates))
# what is the amount of most common coordinate
counts = Counter(cleaned_coordinates)
print(counts.most_common(1))
# use pandas for plotting coordinates as categorical values
df = pd.DataFrame([ str(c[0]) + str(c[1]) for c in coordinates], columns=["coordinates"])
print(df)
df.coordinates = df.coordinates.astype("category")
print(df.coordinates)
plt.matshow(np.matrix(df.coordinates.cat.codes).reshape((height, width)))
plt.show()
