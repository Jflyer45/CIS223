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

    # Jeremy Fischer's Part
    def alternateListJoin(self, q):
        # Set up a temp linkedList to then later replace self.head
        listJoin = LinkedList()
        # While either lists are not at the end alternate adding to listJoin
        while self.head is not None or q.head is not None:
            listJoin.insert_at_head(self.head.data)
            self.head = self.head.next
            listJoin.insert_at_head(q.head.data)
            q.head = q.head.next
        # Once either head is None, add the remaining data from the list that head is not none.
        if q.head is None:
            while self.head is not None:
                listJoin.insert_at_head(self.head.data)
                self.head = self.head.next
        else:
            while q.head is not None:
                listJoin.insert_at_head(q.head.data)
                q.head = q.head.next

        # Finally replace the original list with the new one
        self.head = listJoin.head

    # Function to print linked list
    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        print(" ")
