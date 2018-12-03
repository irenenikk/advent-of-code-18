import re
input = open("input1.txt", "r").read().splitlines()
# save the amount of squared for each coordinate
coordinates = {}
overlapped = set()
ids = set()
for square in input:
    cleaned = re.sub('[#@,:x]', ',', re.sub('[ ]', '', square))
    ide, xstart, ystart, dx, dy = list(map(int, cleaned.split(',')[1:]))
    ids.add(ide)
    for x in range(xstart, xstart + dx):
        for y in range(ystart, ystart + dy) :
            coord_key = str(x) + ','+ str(y)
            if coord_key in coordinates:
                coordinates[coord_key].add(ide)
                overlapped.add(ide)
                [overlapped.add(over_id) for over_id in coordinates[coord_key]]
            else:
                coordinates[coord_key] = set([ide])
    
print(ids - overlapped)