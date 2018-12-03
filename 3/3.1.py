import re
input = open("input1.txt", "r").read().splitlines()
# save the amount of squared for each coordinate
coordinates = {}
for square in input:
    cleaned = re.sub('[#@,:x]', ',', re.sub('[ ]', '', square))
    splitted = cleaned.split(',')[1:]
    _, xstart, ystart, dx, dy = list(map(int, cleaned.split(',')[1:]))
    for x in range(xstart, xstart + dx):
        for y in range(ystart, ystart + dy) :
            coord_key = str(x) + ','+ str(y)
            if coord_key in coordinates:
                coordinates[coord_key] += 1
            else:
                coordinates[coord_key] = 1
print(len(list(filter(lambda x: x > 1, coordinates.values()))))
