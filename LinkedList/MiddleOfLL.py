class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def push(head, val):
    new_node = Node(val)
    if not head:
        head = new_node
        return
    new_node.next = head
    head = new_node
    return head


def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("END")


def middleLL(head):
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    return prev, slow


head = Node(5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)

print("Original LL: ", end='')
printLL(head)

prev, ans = middleLL(head)

print("Previous Node: ", prev.val)
print("Middle of LL: ", ans.val)
print("Next to middle: ", ans.next.val)
