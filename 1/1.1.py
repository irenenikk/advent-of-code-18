from functools import reduce
input = list(map(int, open("input1.txt", "r").read().splitlines()))
print(reduce(lambda x, y: x + y, input, 0))