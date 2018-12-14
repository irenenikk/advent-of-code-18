import math
from itertools import product
import numpy as np

inp = 9306

def get_power_level(x, y):
    # according to the exercise instructions
    rack_id = x + 10
    power = rack_id * y + inp
    power *= rack_id
    power = math.floor(power/100) % 10
    power -= 5
    return power

max_power_sum = 0
max_left_corner = -1
power_sums = np.zeros((300, 300))
# initialize sums to recognizable value
power_sums[:]  = -1
n = 300
for x in range(1, n - 3):
    for y in range(1, n - 3):
        # define cells inside grid
        xs = range(x, x+3)
        ys = range(y, y+3)
        grid_sum = 0
        for xi, yi in product(xs, ys):
            # store the power sums in order to avoid unnecessary calculations
            if power_sums[yi, xi] == -1:
                power_sum = get_power_level(xi, yi)
                power_sums[yi, xi] = power_sum
                grid_sum += power_sum
            else:
                grid_sum += power_sums[yi, xi]
        # store the information we wanted about the max sum
        if grid_sum > max_power_sum:
            max_left_corner = (x,y)
            max_power_sum = grid_sum
print(max_left_corner)