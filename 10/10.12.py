import numpy as np
from functools import reduce
import re
import matplotlib.pyplot as plt

inputs = open("input.txt", "r").read().splitlines()

input_len = len(inputs)

def get_coordinates(inp):
    return np.array(list(map(int, inp[inp.find("<")+1:inp.find(">")].split(', '))))

positions = np.zeros((len(inputs), 2), dtype=int)
velocities = np.zeros((len(inputs), 2), dtype=int)
# parse the input
for i, inp in enumerate(inputs):
    pos, vel = inp.split("velocity")
    positions[i,] = get_coordinates(pos)
    velocities[i, ] = get_coordinates(vel)
old_width = 9999999
j = 0
while (True):
    min_x, max_x = min(positions[:, 0]), max(positions[:, 0])
    min_y, max_y = min(positions[:, 1]), max(positions[:, 1])
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    # if the width starts to increase, then we probably
    # reached the message the last round
    if old_width < width:
        break
    old_width = width
    # don't draw too big a matrix
    draw_picture = width < 1000 and height < 1000
    # present the picture as a matrix
    if draw_picture:
        picture = np.zeros((max_y + 1, max_x + 1), dtype=int)
    for i in range(input_len):
        x = positions[i,0]
        y = positions[i,1]
        if draw_picture:
            picture[y, x] = 1
    # update the positions according to velocities
    for i in range(input_len):
        positions[i,] =  positions[i,0] + velocities[i,0], positions[i,1] + velocities[i,1]
    j += 1

# the answer is the last round
print(j-1)
if draw_picture:
    plt.matshow(picture)
    plt.show()
