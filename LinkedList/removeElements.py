class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def push(head, new_val):
    new_node = Node(new_val)
    if head == None:  # If empty LL
        head = new_node
        return
    new_node.next = head
    head = new_node
    return head


def removeElements(head, val):
    # Notes:
    # if head.next => current element the head => prev element
    # and head.next.next => next element ie right adjacent node
    if not head:
        return head

    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    if head.val == val:
        head = head.next

    return head


def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("NULL")


head = Node(6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 6)
head = push(head, 2)
head = push(head, 6)


print("Original List: ", end="")
printLL(head)

head = removeElements(head, 6)

print("Modified List: ", end="")
printLL(head)
