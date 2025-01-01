class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return ""+str(self.head.data)

    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("END")

    def display_head(self, head):
        while (head != None):
            print(head.data, "->", end=" ")
            head = head.next
        print("END")

    def insert(self, new_data, index):

        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
            return

        if index == 0:  # InsertFirst
            new_node = Node(new_data)
            new_data.next = self.head
            self.head = new_node
            self.size += 1
            return

        if index == self.size:  # InsertLast
            new_node = Node(new_data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return

        # Insert in between
        temp = self.head  # For traversing
        for _ in range(1, index):
            temp = temp.next

        new_node = Node(new_data)
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
