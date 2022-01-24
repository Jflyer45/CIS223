# Writen By: Jeremy Fischer, , and
from Problem1 import TwoStack
from Problem2 import Queue

#Queue Testing
myQueue = Queue(8)

myQueue.Enqueue(1)
myQueue.Enqueue(2)
myQueue.Enqueue(3)
myQueue.Enqueue(4)
myQueue.Enqueue(5)
myQueue.Enqueue(6)
print(myQueue.Dequeue())
print(myQueue.Dequeue())
print(myQueue.Dequeue())
print(myQueue.Dequeue())
print(myQueue.Dequeue())
print(myQueue.Dequeue())
# myQueue.Enqueue(1)
# myQueue.Enqueue(2)
# myQueue.Enqueue(3)
# myQueue.Dequeue()
# myQueue.Dequeue()
#
print("Head: " + str(myQueue.head))
print("Tail: " + str(myQueue.tail))
print(myQueue.myStack.array)
#
# # Smaller Queue Testing
# otherQu = Queue(2)
# otherQu.Enqueue(1)
# otherQu.Enqueue(2)
# otherQu.Dequeue()
#
# print(otherQu.myStack.array)
#
# # TwoStack Testing
# testCase = TwoStack(2, 3)
#
# testCase.Push1(1)
# testCase.Push1(2)
#
# testCase.Push2(3)
# testCase.Push2(4)
# testCase.Push2(5)
# testCase.Push2(466)
# testCase.Push2(13241234)
# print(testCase.head2)
#
# print(testCase.array)
#
# print(testCase.isFull1())
# print(testCase.isFull2())


# Testing for NONE
# myQueue = Queue(4)
# myQueue.Enqueue(None)
# myQueue.Enqueue(None)
# myQueue.Enqueue(None)
# myQueue.Enqueue(3)
# print(myQueue.myStack.array)
#
# myQueue.Dequeue()
# myQueue.Dequeue()
# myQueue.Dequeue()
# print(myQueue.Dequeue())
# print(myQueue.myStack.array)



