input = list(map(int, open("input1.txt", "r").read().splitlines()))
freqs = {}
freq = 0
i = 0
while (True):
    freq += input[i]
    if  freq not in freqs:
        freqs[freq] = 0
    else:
        print(freq)
        break
    i += 1
    if i == len(input):
        i = 0
