from BasicOperations import LinkedList

LL = LinkedList()

LL.insertAtBeginning(1)
LL.insertAtBeginning(2)
LL.insertAtBeginning(3)
LL.insertAtBeginning(4)
LL.insertLast(0)
LL.insertAfter(LL.head.next, 100)
LL.print()
print("Length of Linked List: ", LL.getCount())

print("Head.data: ", LL.head.data)
print("Head.next.data: ", LL.head.next.data)
print("Element found") if LL.search(100) else print("Element not found")
print("Element found") if LL.search_recur(
    LL.head, 100) else print("Element not found")
LL.sortLL()
print("After Sort: ")
LL.print()
LL.deleteFront()
print("Delete front")
LL.print()
LL.deleteEnd()
print("Delete End")
LL.print()
