class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head


def print_LL(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("NULL")


def delete(head, pos):
    if not head:
        print("Empty LL!")
        return
    index = 0
    while head.next and index < pos:
        prev = head
        head = head.next
        index += 1
    if index < pos:
        print("Index doesn't exists!")
    elif index == 0:
        head = head.next  # if Only 1 element exists.
    else:
        prev.next = head.next


head = None
head = push(head, 7)
head = push(head, 1)
head = push(head, 3)
head = push(head, 2)
head = push(head, 8)

print("Created Linked List: ", end="")
print_LL(head)
delete(head, 4)
print("Linked List after Deletion at position 4: ", end="")
print_LL(head)
print("Trying Invalid pos: ")
delete(head, 20)

