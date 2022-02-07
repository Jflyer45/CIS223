from Assignment2Problem1 import LinkedList

# TODO Test code below

myList = LinkedList()

myList.insert_at_head(1)
myList.insert_at_head(2)
myList.insert_at_head(3)
print("=== List1 ===")
myList.printList()

myList2 = LinkedList()
myList2.insert_at_head(4)
myList2.insert_at_head(5)
myList2.insert_at_head(6)
myList2.insert_at_head(7)
print("=== List2 ===")
myList2.printList()

myList.alternateListJoin(myList2)
print("=== List1 But Joined ===")
myList.printList()
print()

print("=== Testing printRange() ===")
print("Printing the range 1-2 of a empty list")
myOtherList = LinkedList()
myOtherList.printRange(1, 2)

print("Printing the ranges -1-5 of List1")
myList.printRange(-1, 5)

print("Printing the ranges .23-5 of List1")
myList.printRange(.22, 5)

print("Printing the ranges a-5 of List1")
myList.printRange("a", 5)

print("Printing the ranges 2-5 of List1")
myList.printRange(2, 5)


print("=== List1 ===")
myList.printList()

print("=== List2 ===")
myList2.printList()
