inputs = open("input.txt", "r").read()

# add each character to stack
# with a new character, check if reacts with the top element of stack

def react(a, b):
    if a.isupper() and a.lower() == b:
        return True
    if b.isupper() and b.lower() == a:
        return True
    return False    


stack = list()
for char in inputs:
    if (len(stack) == 0):
        stack.append(char)
        continue
    # peek stack
    top = stack[-1]
    if react(char, top):
        stack.pop()
    else:
        stack.append(char)
print(len(stack))