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

        #check to make sure that the original list is not empty
        while (headOriginalCopy != None):

            if(headListToMergeCopy == None):
                break
            else:
                #create copies of the original next node and next of the merge list
                nextOriginal = headOriginalCopy.next
                nextListToMerge = headListToMergeCopy.next

                #now we make sure that the pointed nodes are lined up
                headOriginalCopy.next = headListToMergeCopy
                #next original is now the head
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

TestList = LinkedList()

print("\n Testing pring from the empty list")
TestList.printRange(1,5)


print("Testing Normal Case \n=========================")
TestList.insert_at_head(101)
TestList.insert_at_head(201)
TestList.insert_at_head(301)
TestList.insert_at_head(401)


print("Print Range 1 - 3")
TestList.printRange(1,3)

print("\n")
TestList.insert_at_head(501)
TestList.printRange(1,3)

print("\n Printing Range Test")
print('===============')
print('Having same range 2,2')
TestList.printRange(2,2)

print('\nhaving reversed ragne 3,1')
TestList.printRange(3,1)

print("\nPrinting range over size of the list")
TestList.printRange(1,30)

print('\nHaving Decimal number in range')
TestList.printRange(1,2.5)

print('\nHaving Negative number in ragne')
TestList.printRange(1, -5)


# print("\nPrinting Range starting from over the size of the list")
# TestList.printRange(30,50) # Error Occurred: AttributeError at temp=temp.next
# t = 10000
t=10
print('\n Adding large amount of item into a list ')
LargeList = LinkedList()
for i in range(t):
    LargeList.insert_at_head(i)
LargeList.printRange(1, t)
# --No Error Occurred --


print('... End of LinkedList Class Testing ...')


#Alternate List Testing
print('====================')
print('Alternate List Testing...')

# Defining Function
def showList():
    print('printing List P')
    TestingP.printList()
    print('printing List Q')
    TestingQ.printList()

#========================


print('\n\n <<All process merging Q into P>>')
print('\n *Alternating lists with same size')
print('... initializing ...')
    # Initialization for testing
TestingP = LinkedList()
TestingQ = LinkedList()

print('inputting nodes into lists...')

TestingP.insert_at_head(11)
TestingP.insert_at_head(9)
TestingP.insert_at_head(7)
TestingP.insert_at_head(5)
TestingP.insert_at_head(3)
TestingP.insert_at_head(1)

TestingQ.insert_at_head(12)
TestingQ.insert_at_head(10)
TestingQ.insert_at_head(8)
TestingQ.insert_at_head(6)
TestingQ.insert_at_head(4)
TestingQ.insert_at_head(2)
showList()

print('\n AltJoin When Both have the same size')
TestingP.alternateListJoin(TestingQ)
showList()

print('\n *Alternating lists with different size')

print('\n\t1. Size of P > Size of Q')
print('... initializing ...')

    # Initialization for testing
TestingP = LinkedList()
TestingQ = LinkedList()

print('inputting nodes into lists...')

TestingP.insert_at_head(15)
TestingP.insert_at_head(13)
TestingP.insert_at_head(11)
TestingP.insert_at_head(9)
TestingP.insert_at_head(7)
TestingP.insert_at_head(5)
TestingP.insert_at_head(3)
TestingP.insert_at_head(1)

TestingQ.insert_at_head(12)
TestingQ.insert_at_head(10)
TestingQ.insert_at_head(8)
TestingQ.insert_at_head(6)
TestingQ.insert_at_head(4)
TestingQ.insert_at_head(2)
showList()

print('\nExecute AlternateListJoin...\n\n')
TestingP.alternateListJoin(TestingQ)
showList()

print('\n\t2. Size of P < Size of Q')
print('... initializing ...')
    # Initialization for testing
TestingP = LinkedList()
TestingQ = LinkedList()

print('inputting nodes into lists...')

TestingP.insert_at_head(11)
TestingP.insert_at_head(9)
TestingP.insert_at_head(7)
TestingP.insert_at_head(5)
TestingP.insert_at_head(3)
TestingP.insert_at_head(1)

TestingQ.insert_at_head(16)
TestingQ.insert_at_head(14)
TestingQ.insert_at_head(12)
TestingQ.insert_at_head(10)
TestingQ.insert_at_head(8)
TestingQ.insert_at_head(6)
TestingQ.insert_at_head(4)
TestingQ.insert_at_head(2)
showList()

print('\nExecute AlternateListJoin\n\n')
TestingP.alternateListJoin(TestingQ)
showList()