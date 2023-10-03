def isEmpty(stack):
    return len(stack) == 0


def push(stack, val):
    stack.append(val)
    print(val, "pushed to stack", stack)


def pop(stack):
    if isEmpty(stack):
        return "Stack is empty"
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return "Stack is empty"
    return stack[len(stack) - 1]


stack = []
print(stack)
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
print("peek is: ", peek(stack))
print("popped item: ", pop(stack))
print("Stack is: ", stack)
