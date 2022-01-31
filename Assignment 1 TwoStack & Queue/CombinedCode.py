# This is the file we will turn to txt to turn in

class TwoStack:
    def __init__(self, size1, size2):
        self.size1 = size1
        self.size2 = size2
        self.TotalSize = size1 + size2
        self.My_stack = [None] * self.TotalSize
        self.tos1 = -1
        self.tos2 = self.TotalSize

    def push1(self, key):
        if self.isFull1() == True:
            return False

        else:
            self.tos1 += 1
            self.My_stack[self.tos1] = key
            return True

    def push2(self, key):
        if self.isFull2() == True:
            return False

        else:
            self.tos2 -= 1
            self.My_stack[self.tos2] = key
            return True

    def pop1(self):
        if self.isEmpty1() == True:
            return False

        else:
            val = self.peek1()
            self.My_stack[self.tos1] = None
            self.tos1 -= 1
            return val

    def pop2(self):
        if self.isEmpty1() == True:
            return False

        else:
            val = self.peek2()
            self.My_stack[self.tos2] = None
            self.tos2 += 1
            return val

    def isFull1(self):
        if self.tos1 >= self.size1 - 1:
            return True
        else:
            return False

    def isFull2(self):
        if self.tos2 <= self.size1:
            return True
        else:
            return False

    def isEmpty1(self):
        if self.tos1 == -1:
            return True
        else:
            return False

    def isEmpty2(self):
        if self.tos2 == self.TotalSize:
            return True
        else:
            return False

    def peek1(self):
        if self.isEmpty1() == True:
            return "Stack1 is Empty. Unable to peek"
        else:
            return self.My_stack[self.tos1]

    def peek2(self):
        if self.isEmpty2() == True:
            return "Stack2 is Empty. Unable to peek"
        else:
            return self.My_stack[self.tos2]

class Queue():
    def __init__(self, size):
        # Ensures size is not negative, zero, or odd. If so default 2
        if size % 2 != 0 or size < 0:
            size = 2

        self.size = size
        self.myStack = TwoStack(size, size)

    # Adds numbers to the first stack while it's not full
    def Enqueue(self, data):
        if not self.isFull() == True:
            self.myStack.push1(data)
            return f"Enqueue {data} Success!"
        
        else:
            return False
            raise AssertionError
            assert "Enqueue Failed"

    def Dequeue(self):
        while self.myStack.isEmpty1() == False:
            self.myStack.push2(self.myStack.pop1())
        dataToReturn = self.myStack.peek2()
        while self.myStack.isEmpty2() == False:
            self.myStack.push1(self.myStack.pop2())
        return dataToReturn

    # Simply checks if stack1 is full
    def isFull(self):
        return self.myStack.isFull1()

    # Simply checks if both stacks are empty
    def isEmpty(self):
        return self.myStack.isEmpty1() and self.myStack.isEmpty2()

#TODO Write Driver/Test code below

myQueue = Queue(4)

print(myQueue.Enqueue(101))
print(myQueue.Enqueue(102))
print(myQueue.Enqueue(103))
print(myQueue.Enqueue(104))

print(myQueue.Dequeue())