class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def push(head, new_val):
    new_node = Node(new_val)
    if not head:
        head = new_node
    new_node.next = head
    head = new_node
    return head


def printLL(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("END")


def NthNodeFromEnd(head, val):

    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next

    curr = head
    i = 0

    if val > size:  # If asked index is greater than size of LL
        return 0

    while curr:
        if i == size - val:
            return curr.val
        i += 1
        curr = curr.next


head = Node(10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
head = push(head, 50)
head = push(head, 60)
head = push(head, 70)

print("Original LL: ", end='')
printLL(head)

ans = NthNodeFromEnd(head, 2)

print("2nd Node from end is -> ", ans) if ans else print("2nd node not found")

ans = NthNodeFromEnd(head, 9)

print("9th Node from end is -> ", ans) if ans else print("9th node not found")
