from LL import LinkedList


def reverseLL(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


ll = LinkedList()
ll.insert(new_data=10, index=0)
ll.insert(new_data=20, index=1)
ll.insert(new_data=30, index=2)
ll.insert(new_data=40, index=3)
ll.insert(new_data=50, index=4)
ll.insert(new_data=60, index=5)
ll.display()
new_head = reverseLL(ll.head)
ll.display_head(new_head)
