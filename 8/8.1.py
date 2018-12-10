inputs = map(int, open("input.txt", "r").read().split())

metadata_sum = 0

def walk_tree(tree, index):
    global metadata_sum
    n_children, n_metadata = tree[index:index+2]
    info = tree[index+2:]
    # base case
    if n_children == 0:
        # return the current metadata sum and index after metadata
        return metadata_sum + sum(info[:n_metadata]), index + n_metadata
    # repeat for all children
    for _ in range(n_children):
        # skip the no of children and metadata
        metadata_sum, index = walk_tree(tree, index+2) 
    return metadata_sum + sum(tree[index+2:index+2 + n_metadata]), index + n_metadata

# start walking from index 0
metadata_sum, _ = walk_tree(inputs, 0)
print(metadata_sum)