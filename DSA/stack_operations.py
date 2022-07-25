
# stack DSA

def createStack():
    arr = []
    return arr


def push(stack, value):
    stack.append(value)
    print(value + " added to stack")


def pop(stack):
    if(stack == -1):
        print("Stack is empty")
    else:
        stack.pop()


def print_stack(stack):
    for i in stack:
        print(i)


new_stack = createStack()
push(new_stack, "A")
push(new_stack, "B")
push(new_stack, "C")
print_stack(new_stack)

pop(new_stack)
print_stack(new_stack)
