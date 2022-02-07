# Hello Sungjae
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
    def printRange(self, x, y):
        # We need to make a copy to not mess with the other one
        temp = self.head

        if self.head is None:
            print("No Item in range")

        # Data verification
        if x > y or x <= 0:
            print("Invalid Range")
        else:
            # Input is valid
            # Iterates through the linked list until it gets to the correct index
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

            # Then continues to prints each node until it reaches y or null
            # Checks to make sure if the range it not itself
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
        selfHeadCopy = self.head
        qHeadCopy = q.head

        # swap their positions until one finishes off
        while selfHeadCopy != None and qHeadCopy != None:
            # Save next pointers
            selfNext = selfHeadCopy.next
            qNext = qHeadCopy.next

            # make q_curr as next of p_curr
            qHeadCopy.next = selfNext  # change next pointer of q_curr
            selfHeadCopy.next = qHeadCopy  # change next pointer of p_curr

            # update current pointers for next iteration
            selfHeadCopy = selfNext
            qHeadCopy = qNext
            q.head = qHeadCopy


    # Function to print linked list
    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        # print(" ")
