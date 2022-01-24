# Writen By: Jeremy Fischer, , and

from Problem1 import TwoStack

class Queue():
    def __init__(self, size):
        # Ensures size is not negative, zero, or odd. If so default 2
        if size % 2 != 0 and size > 0:
            size = 2

        self.size = size
        self.myStack = TwoStack(size, size)

    def Enqueue(self, data):
        self.myStack.Push1(data)

    def Dequeue(self):
        while not self.myStack.isEmpty1():
            self.myStack.Push2(self.myStack.Pop1())
        dataToReturn = self.myStack.Pop2()
        while not self.myStack.isEmpty2():
            self.myStack.Push1(self.myStack.Pop2())
        return dataToReturn

    # Simply checks if both stacks are full
    def isFull(self):
        return self.myStack.isFull1() and self.myStack.isFull2()

    # Simply checks if both stacks are empty
    def isEmpty(self):
        return self.myStack.isEmpty1() and self.myStack.isEmpty2()

myStack = TwoStack(2, 2)
