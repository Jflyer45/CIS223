# Writen By: Jeremy Fischer, , and
#from Problem1 import TwoStack
#from Problem2 import Queue
from CombinedCode import TwoStack, Queue
print('---------------Start----------------')
myStack = TwoStack(3,3)

print(f"Push 1 into stack 1: {myStack.push1(101)}")
print(f"Push 2 into stack 1: {myStack.push1(102)}")
print(f"Push 3 into stack 1: {myStack.push1(103)}")
print(f"Push 4 into stack 1: {myStack.push1(104)}")
#not allowed
print("\n\t **Stack 2 push**")
print(f"Push item into stack 2: {myStack.push2(201)}")
print(f"Push item into stack 2: {myStack.push2(202)}")
print(f"Push item into stack 2: {myStack.push2(203)}")
print(f"Push item into stack 2: {myStack.push2(204)}") # not allowed

print("\t\n --Pop Stack 2--")
print("Pop Stack 2 Result:")
print(myStack.pop2()) # 203 should be gone

print()



print("********Queue Testing********")
myQueue = Queue(6)

print(f"The Size of Queue: {myQueue.size}") 

print(myQueue.Enqueue(101))
print(myQueue.Enqueue(201))
print(myQueue.Enqueue(301))
print(myQueue.Enqueue(401))


dqNumber = myQueue.Dequeue()

print(f"DQ: {dqNumber}")



