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
        # We need to make a copy to not mess with the other one
        temp = self.head

        # Data verification
        if x > y or x <= 0:
            print("Invalid Range")
        else:
            # Input is valid
            counter = 1
            while True:
                if counter == x:
                    print(temp.data)
                    temp = temp.next
                    counter += 1
                    break
                else:
                    temp = temp.next
                    counter += 1

            if x != y:
                while temp is not None:
                    if counter == y:
                        print(temp.data)
                        break
                    else:
                        print(temp.data)
                        counter += 1
                        temp = temp.next

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
