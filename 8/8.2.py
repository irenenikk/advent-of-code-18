inputs = map(int, open("input.txt", "r").read().split())

def walk_tree(tree, index):
    n_children, n_metadata = tree[index:index+2]
    info = tree[index+2:]
    # base case
    if n_children == 0:
        # return the current metadata sum and index after metadata
        return sum(info[:n_metadata]), index + n_metadata
    # repeat for all children
    children_values = [0] * n_children
    for i in range(n_children):
        value, index = walk_tree(tree, index+2) 
        children_values[i] = value
    return sum([children_values[meta - 1] for meta in tree[index+2:index+2 + n_metadata] if meta > 0 and meta <= n_children]), index + n_metadata

# start walking from index 0
value_sum, _ = walk_tree(inputs, 0)
print(value_sum)
