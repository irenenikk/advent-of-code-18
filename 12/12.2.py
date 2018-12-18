import re
import math
import numpy as np

inputs = open("input.txt", "r").read().splitlines()

def get_index_sum(state, index_of_zero):
    return sum([i - index_of_zero for i in np.where(np.array(state) == '#')[0]])

state = re.sub('[^#.]', '', inputs[0])
# there's an additional newline
info = inputs[2:]

plant_evolutions = {}

# store the length of the evolution infos in a separate variable
info_len = -1

for evolution in info:
    infos = evolution.split(' => ')
    plant_evolutions[infos[0]] = infos[1]
    info_len = len(infos[0])

state = list('.' * info_len + state +  '.' * info_len)

generations = 50000000000
# store the index of pot zero in order to calculate the numbers of pots
index_of_zero = info_len

last_state_sum = 0
pots = 0
for gen in range(generations):
    # construct a new state instead of modifying old one
    # use a list for easy modification
    new_state = ['.'] * len(state)
    # print(''.join(state))
    for i in range(len(state) - info_len):
        plants = state[i:i+info_len]
        plant_string = ''.join(plants)
        if plant_string in plant_evolutions:
            # change the middle pot according to evolution instruction
            middle = int(math.floor(info_len/2))
            new_state[i+middle] = plant_evolutions[plant_string]
    # always keep a buffer of empty pots at both ends
    if '#' in  ''.join(new_state[-info_len:]):
        new_state = new_state + ['.'] * info_len 
    if '#' in  ''.join(new_state[:info_len]):
        new_state = ['.'] * info_len + new_state
        index_of_zero += info_len
    state = new_state
    # see how many pots there are
    state_sum = get_index_sum(state, index_of_zero)
    # check if the pots have just moved to the right (which they seem to do)
    pots = state.count('#')
    if state_sum == last_state_sum + pots:
        break
    last_state_sum = get_index_sum(state, index_of_zero)
# transform indexes back to original scale
print(get_index_sum(state, index_of_zero) + (generations - gen - 1)*pots)
