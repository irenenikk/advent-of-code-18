import math
from itertools import product
import numpy as np

# this solution is based on the sum matrix instructions here: 
# https://www.cs.helsinki.fi/u/ahslaaks/ncpc/sumtaul.html

inp = 9306

def get_power_level(x, y):
    # according to the exercise instructions
    rack_id = x + 10
    power = rack_id * y + inp
    power *= rack_id
    power = math.floor(power/100) % 10
    power -= 5
    return power

def build_sum_matrix(shape):
    sum_matrix = np.zeros(shape)
    for i in range(shape[0]):
        row = 0
        for j in range(shape[1]):
            row += get_power_level(i, j)
            sum_matrix[i][j] = row
            if i > 0:
                sum_matrix[i][j] += sum_matrix[i-1][j]
    return sum_matrix
    
n = 300
sum_matrix = build_sum_matrix((n, n))
max_power_sum = 0
max_left_corner = -1
max_size = -1
# go through possible sums and print biggest
for size in range(1, n + 1):
    # x and y denote the upper left corner
    for x in range(1, n - size):
        for y in range(1, n - size):
            xend = x + size - 1
            yend = y + size - 1
            # print('start: ', (x, y))
            # print('end: ', (xend, yend))
            grid_sum = sum_matrix[xend][yend]
            if x > 0:
                grid_sum -= sum_matrix[x-1][yend]
            if y > 0:
                grid_sum -= sum_matrix[xend][y -1]
            if x > 0 and y > 0:
                grid_sum += sum_matrix[x -1][y -1]
            if grid_sum > max_power_sum:
                max_left_corner = (x,y)
                max_power_sum = grid_sum
                max_size = size
print(max_left_corner, max_size)
