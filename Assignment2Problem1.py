class LinkedList(object):
    def __init__(self):
        # head of the list
        self.head = None

    # Linked list node
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def insert_at_head(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    # TODO
    def printRagnge(self, x, y):
        # TODO validate ranges, make sure x < y, x > 0, ensure y < length+
        print(x)

    # TODO
    def alternateListJoin(self, q):
        if self.head is None:
            return q
        if q.head is None:
            return self.head

        listJoin = LinkedList()
        while self.head is not None or q.head is not None:
            listJoin.insert_at_head(self.head.data)
            self.head = self.head.next
            listJoin.insert_at_head(q.head.data)
            q.head = q.head.next

        if q.head is None:
            while self.head is not None:
                listJoin.insert_at_head(self.head.data)
                self.head = self.head.next
        else:
            while q.head is not None:
                listJoin.insert_at_head(q.head.data)
                q.head = q.head.next

        self.head = listJoin.head

    # Function to print linked list
    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        print(" ")
