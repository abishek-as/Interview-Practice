class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Notes:
    # if head.next => current element the head => prev element
    # and head.next.next => next element ie right adjacent node


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def search_recur(self, li, key):
        if not li:
            return False
        if li.data == key:
            return True
        return self.search_recur(li.next, key)

    def insertAtBeginning(self, data):
        new_node = Node(data)  # Node Created

        if self.head == None:  # Check for Empty LL
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insertLast(self, data):
        new_node = Node(data)  # Node Created

        if self.head == None:  # Check for Empty LL
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node  # assigning new node to last

    def insertAfter(self, prev_node, data):
        if prev_node == None or self.search(data):
            print("Node Doesn't exists.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def sortLL(self):
        i = self.head
        j = Node(None)

        if self.head is None:
            return
        while i:
            # j points to the node next to current
            j = i.next
            while j:
                if i.data > j.data:
                    i.data, j.data = j.data, i.data
                j = j.next
            i = i.next

    def getCount(self):
        tmp = self.head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def deleteFront(self):
        if not self.head:
            print("Empty LL!, Nothing to delete")
            return

        self.head = self.head.next

    def deleteAfter(self):
        pass

    def deleteEnd(self):
        if self.head == None:
            print("Empty LL!, Nothing to delete")
        if self.head.next == None:  # If only 1 element is present in LL
            self.head = None

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data, "->", end=" ")
            tmp = tmp.next
        print("None")
