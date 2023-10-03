from BasicOperations import LinkedList


def removeDuplicates(head):
    if not head:
        print("Empty LL!")
        return

    while head.next:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next


ll = LinkedList()
ll.insertAtBeginning(4)
ll.insertAtBeginning(4)
ll.insertAtBeginning(3)
ll.insertAtBeginning(3)
ll.insertAtBeginning(3)
ll.insertAtBeginning(2)
ll.insertAtBeginning(2)
ll.insertAtBeginning(1)
print("Original LL: ")
ll.print()
removeDuplicates(ll.head)
print("Unique LL: ")
ll.print()
