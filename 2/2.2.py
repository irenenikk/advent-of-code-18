import re

input = open("input1.txt", "r").read().splitlines()

def get_all_versions(word):
    for i in range(0, len(word)):
        yield word[0:i] + '?' + word[i+1:]

version_set = set()
for word in input:
    set_length = len(version_set)
    for version in get_all_versions(word):
        version_set.add(version) 
        if (len(version_set) == set_length):
            print(re.sub('[^A-Za-z0-9]+', '', version))
        set_length = len(version_set)
