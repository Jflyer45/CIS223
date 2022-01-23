# Writen By: Jeremy Fischer, , and

from Problem1 import TwoStack

class Queue():
    def __init__(self, size):
        #TODO Check size is good
        self.size = size
        self.myStack = TwoStack(size//2, size//2)
        self.head = 0
        self.tail = 0

        self.mid = (size//2) - 1

    def Enqueue(self, data):
        # Check to see if there is available spot at head, else do nothing
        if self.myStack.array[self.head] is None:
            if self.head <= self.mid:
                TwoStack.Push1(self.myStack, data)
            else:
                TwoStack.Push2(self.myStack, data)
            self.__traverseHead()

    def Dequeue(self):
        dataToReturn = None
        # Checks to see if there is data to deque, else do nothing
        if self.myStack.array[self.tail] is not None:
            dataToReturn = self.myStack.array[self.tail]
            self.myStack.array[self.tail] = None
            self.__traverseTail()
            if self.myStack.head1 == self.mid:
                self.myStack.head1 = 0
            if self.myStack.head2 == self.mid + 1:
                self.myStack.head2 = self.size -1


        return dataToReturn

    def __traverseTail(self):
        if self.tail == self.mid:
            self.tail = self.size - 1
        elif self.tail == self.mid + 1:
            self.tail = 0
        elif self.tail < self.mid:
            self.tail += 1
        else:
            self.tail -= 1

    def __traverseHead(self):
        if self.head == self.mid:
            self.head = self.size - 1
        elif self.head == self.mid + 1:
            self.head = 0
        elif self.head < self.mid:
            self.head += 1
        else:
            self.head -= 1

    # Simply checks if both stacks are full
    def isFull(self):
        return self.myStack.isFull1() and self.myStack.isFull2()

    # Simply checks if both stacks are empty
    def isEmpty(self):
        return self.myStack.isEmpty1() and self.myStack.isEmpty2()

myStack = TwoStack(2, 2)
