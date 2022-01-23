# Writen By: Jeremy Fischer, , and
from Problem1 import TwoStack
from Problem2 import Queue

myQueue = Queue(6)

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


print("Head" + str(myQueue.head))

myQueue.Enqueue(7)
myQueue.Enqueue(8)
myQueue.Enqueue(9)
myQueue.Enqueue(10)

myQueue.Dequeue()
myQueue.Enqueue(11)
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()



print(myQueue.myStack.array)




# testCase = TwoStack(2, 3)
#
# testCase.Push1(1)
# testCase.Push1(2)
#
# testCase.Push2(5)
# testCase.Push2(4)
# testCase.Push2(4)
# testCase.Push2(466)
# testCase.Push2(13241234)
# print(testCase.head2)
#
# print(testCase.array)
#
# print(testCase.isFull1())
# print(testCase.isFull2())



