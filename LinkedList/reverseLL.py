class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def push(head, new_val):
    new_node = Node(new_val)
    if head == None:
        head = new_node
        return
    new_node.next = head
    head = new_node
    return head


def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("NULL")


def reverseLL(head):
    prev = None
    current = head

    while current:
        adj = current.next  # storing the adjacent node
        current.next = prev  # current should point to prev
        prev = current  # traverse prev to current
        current = adj  # traverse current to adjacent node
    return prev  # prev contains last node coz current is null


head = Node(10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
head = push(head, 50)
head = push(head, 60)

print("\nOriginal LL: ", end="")

new_head = reverseLL(head)
print("Reversed LL: ", end="")
