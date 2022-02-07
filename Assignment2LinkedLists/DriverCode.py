from Assignment2Problem1 import LinkedList

# TODO Test code below

myList = LinkedList()

myList.insert_at_head(1)
myList.insert_at_head(2)
myList.insert_at_head(3)
myList.printList()

myList2 = LinkedList()
myList2.insert_at_head(4)
myList2.insert_at_head(5)
myList2.insert_at_head(6)

myList.alternateListJoin(myList2)
myList.printList()
print()
myList.printRange(0,100)

print("Now printing the list")
myList.printList()
