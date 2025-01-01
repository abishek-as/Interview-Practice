class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def push(head, new_val):
    new_node = Node(new_val)
    if not head:
        head = new_node
        return
    new_node.next = head
    head = new_node
    return head


def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("END")


def NthNode(head, index):
    current = head
    count = 0

    while current:
        if count == index:
            return current.val  # element found at given index
        count += 1
        current = current.next

    return 0  # No element found


head = Node(10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
head = push(head, 50)
head = push(head, 60)
head = push(head, 70)

print("Original LL: ", end='')
printList(head)
x = 4
ans = NthNode(head, x)

print(x, "th Node is ->", ans) if ans else print(x, "th Node not found")

x = 9
ans = NthNode(head, x)

print(x, "th Node found at ->", ans) if ans else print(x, "th Node not found")
