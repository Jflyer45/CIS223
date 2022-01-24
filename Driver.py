# Writen By: Jeremy Fischer, , and
from Problem1 import TwoStack
from Problem2 import Queue

myStack = TwoStack(3,3)

myStack.Push1(1)
myStack.Push1(2)
myStack.Push1(3)
myStack.Push1(1)

myStack.Push2(4)
myStack.Push2(5)
myStack.Push2(6)
myStack.Push2(1)

myStack.Pop2()

print(myStack.stacks)
print()

myQueue = Queue(4)

myQueue.Enqueue(1)
myQueue.Enqueue(2)
myQueue.Enqueue(3)
myQueue.Enqueue(4)

myQueue.Dequeue()
print(myQueue.myStack.stacks)

