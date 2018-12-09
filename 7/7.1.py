import re
inputs = open("input.txt", "r").read().splitlines()

# implement topological sort

# build a graph from input
# use a dictionary with key-value-pair denoting an edge from key to value
graph = {}
for info in inputs:
    cleaned = re.sub('[^A-Z]', '', info[1:])
    start, end = cleaned[0], cleaned[1]
    if start not in graph:
        graph[start] = []
    graph[start].append(end)
print(graph)

# https://stackoverflow.com/a/952952
flatten = lambda l: [item for sublist in l for item in sublist]

# implement topological sort using Kahn's algorithm
# assume the graph to be a DAG, othwerise topological sort is not defined
sorted_list = []
# find nodes with no incoming edges
no_incoming = set(filter(lambda node: node not in flatten(graph.values()), graph.keys()))
while len(no_incoming) > 0:
    # make sure to take the first one in alphabetical order
    n = sorted(no_incoming)[0]
    # remove chosen node from list
    no_incoming.remove(n)
    print('n', n)
    sorted_list.append(n)
    # go through nodes connected to n
    if n not in graph:
        break
    for node in graph[n].copy():
        graph[n].remove(node)   
        if node not in flatten(graph.values()):
            no_incoming.add(node)
print(''.join(sorted_list))