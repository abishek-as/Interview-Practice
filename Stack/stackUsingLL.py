class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return True if self.top == None else False

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.top.val

    def push(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.top
        self.top = self.top.next
        popped_node = temp.val
        return popped_node

    def printStack(self):
        temp = self.top
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("END")


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("Original stack: ", end="")
s.printStack()
print("Popping the stack-> ", s.pop())
print("Modified stack: ", end="")
s.printStack()
