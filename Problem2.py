# Writen By: Jeremy Fischer, , and

from Problem1 import TwoStack

# The main idea for this solution is to treat the TwoStack as a circle array. Values will be added to the first stack
# then to the second stack and then back to the first stack if there is room. We must track where the next value will be
# added too and where the next value will be removed from, head and tail do this. Thus, when head is at the end of the
# array (the end of stack 2) it goes back to stack 1.

class Queue():
    def __init__(self, size):
        # Ensures size is not negative, zero, or odd. If so default 2
        if size % 2 != 0 and size > 0:
            size = 2

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
        # Checks to see if there is data to deque, else do nothing.
        if self.myStack.array[self.tail] is not None:
            dataToReturn = self.myStack.array[self.tail]
            self.myStack.array[self.tail] = None
            self.__traverseTail()
            # Heads will gets stuck at the middle if you do not reset them during a dequeue
            if self.myStack.head1 == self.mid:
                self.myStack.head1 = 0
            if self.myStack.head2 == self.mid + 1:
                self.myStack.head2 = self.size - 1
        return dataToReturn

    # With the "circle" array in mind, this increases the tail by 1
    def __traverseTail(self):
        if self.tail == self.mid:
            self.tail = self.size - 1
        elif self.tail == self.mid + 1:
            self.tail = 0
        elif self.tail < self.mid:
            self.tail += 1
        else:
            self.tail -= 1

    # With the "circle" array in mind, this increases the head by 1
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
