# Hello Sungjae
from ast import For
from itertools import count

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

    # Jeremy Fischer's Part
    def printRange(self, x, y):
        # We need to make a copy to not mess with the other one
        temp = self.head
        # Data verification
        if not isinstance(x, int) or not isinstance(y, int):
            print("Must enter whole numbers and only integers.\n")
        elif x > y or x <= 0:
            print("Invalid range, x must be less than y and be greater than 0.\n")
        elif self.head is None:
            print("The linked list is empty.\n")
        # Input is valid
        else:
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

    #Nate Bursch's part
    def alternateListJoin(self,listToMerge):
        headOriginalCopy = self.head
        headListToMergeCopy = listToMerge.head

        #alterante list for the length of self
        while (headOriginalCopy != None):

            if(headListToMergeCopy == None):
                break
            else:
                nextOriginal = headOriginalCopy.next
                nextListToMerge = headListToMergeCopy.next

                # Swaps the pointers of selfHead and qHead
                headOriginalCopy.next = headListToMergeCopy
                headListToMergeCopy.next = nextOriginal

                # Traverse both the linked lists by one
                headOriginalCopy = nextOriginal
                headListToMergeCopy = nextListToMerge

                # We must also update q's head to be whatever the copy is now, as it is decreasing in size
                listToMerge.head = headListToMergeCopy
    # Function to print linked list
    def printList(self):
        if self.head == None:
            print("The linked list is empty.\n")
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        # print(" ")


