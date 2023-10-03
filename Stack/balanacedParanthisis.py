def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "[", "{"]:
            # If opening brackets then push
            stack.append(char)
        else:
            # Closing brackets
            if not stack:  # Stack should not be empty
                return False

            curr_char = stack.pop()
            if curr_char == '(' and char != ")" or curr_char == '{' and char != "}" or curr_char == '[' and char != "]":
                return False

    if stack:
        return False
    return True


expr = "{()}[]()"

# Function call
if areBracketsBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
