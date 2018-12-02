input = open("input1.txt", "r").read().splitlines()
two_times = 0
three_times = 0
for word in input:
    occurences = {}
    for letter in word:
        if letter in occurences:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    if 2 in occurences.values():
        two_times += 1
    if 3 in occurences.values():
        three_times += 1
print(two_times * three_times)