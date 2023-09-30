from LL import LinkedList


def duplicates(LL):
    current = LL.head

    if current is None:
        return

    while current.next:
        if current.data == current.next.data:
            temp = current.next.next
            current.next = temp
        else:
            current = current.next


ll = LinkedList()
ll.insert(new_data=1, index=0)
ll.insert(new_data=1, index=1)
ll.insert(new_data=1, index=2)
ll.insert(new_data=1, index=3)
ll.insert(new_data=2, index=4)
ll.insert(new_data=2, index=5)
ll.insert(new_data=3, index=6)
ll.insert(new_data=3, index=7)
ll.insert(new_data=3, index=8)
ll.display()
duplicates(ll)
ll.display()
