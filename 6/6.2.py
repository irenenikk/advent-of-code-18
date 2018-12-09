import numpy as np
import math
from collections import Counter
import matplotlib.pyplot as plt

from functools import reduce

def get_manhattan_distance(row1, row2, column1, column2):
    return abs(row1 - row2) + abs(column1 - column2)
    
inputs = open("input.txt", "r").read().splitlines()
inputs = [(int(i.split(", ")[0]), int(i.split(", ")[1]))for i in inputs]

min_row = reduce(lambda a, b: a if min(a[0], b[0]) == a[0] else b, inputs)[0]
max_row = reduce(lambda a, b: a if max(a[0], b[0]) == a[0] else b, inputs)[0]
min_col = reduce(lambda a, b: a if min(a[1], b[1]) == a[1] else b, inputs)[1] 
max_col = reduce(lambda a, b: a if max(a[1], b[1]) == a[1] else b, inputs)[1]

# coordinate_matrix = np.zeros((max_row - min_row, max_col - min_col))
distances = []
coordinates = []

# set an arbitrary boundary for the matrix
width  = (max_col - min_col)*2
height = (max_row - min_row)*2

result = 0
distance_limit = 10000

for row in range(0,height):
    for col in range(0, width):
        all_within_range = True
        cumulative_distance = 0
        for i in inputs:
            distance = get_manhattan_distance(row, i[1], col, i[0])
            cumulative_distance += distance
            if cumulative_distance >= distance_limit:
                all_within_range = False
        if all_within_range:
            result += 1
        distances.append(cumulative_distance)
print(result)
dist = np.array(distances)
plt.matshow(np.matrix(dist < distance_limit).reshape((height, width)))
plt.show()