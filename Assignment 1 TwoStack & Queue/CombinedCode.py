# This is the file we will turn to txt to turn in

class TwoStack:
    def __init__(self, size1, size2): # accept two integer numbers to define stack's size
        self.size1 = int(size1)
        self.size2 = int(size2)
        self.TotalSize = size1 + size2 # Define Whole size of the stack
        self.My_stack = [None] * self.TotalSize # putting placeholder as many times as TotalSize
        self.tos1 = -1 # The pointer (top of stack) of stack 1; starting the head of the stack
        self.tos2 = self.TotalSize # The pointer (top of stack) of stack 2; starting from the end of the stack

    def push1(self, key):
        # If the stack1 is full, unable to push, return False
        if self.isFull1() == True:
            return False

        # If the stack isn't full, push the key on the stack1
        # by moving pointer of stack1 to the first place of the stack
        # and replacing the placeholder to the key
        else:
            self.tos1 += 1
            self.My_stack[self.tos1] = key
            return True

        # Same as above
    def push2(self, key):
        if self.isFull2() == True:
            return False

        # Same as above except for the pointer side
        else:
            self.tos2 -= 1
            self.My_stack[self.tos2] = key
            return True

        
    def pop1(self):
        # If the stack1 is empty, unable to pop, return False
        if self.isEmpty1() == True:
            return False
        
        else:
            val = self.peek1() # If the stack isn't Empty, find the value at the pointer, store it
            self.My_stack[self.tos1] = None # and replace the key back to a placeholder
            self.tos1 -= 1 # move the pointer back
            return val # return val

        # Same as pop1 except for the pointer side
    def pop2(self):
        if self.isEmpty1() == True:
            return False

        else:
            val = self.peek2()
            self.My_stack[self.tos2] = None
            self.tos2 += 1
            return val

        # Check the stack is full or not
    def isFull1(self):
        if self.tos1 >= self.size1 - 1: # if the pointer is index at the size of the stack 1, indicates the stack is full
            return True
        else:
            return False

    def isFull2(self):
        if self.tos2 <= self.size1: # if the pointer index is moving to the end of the stack 1, indicates the stack is full.
            return True
        else:
            return False

        # Check the stack is Empty or not
    def isEmpty1(self):
        if self.tos1 == -1: # The pointer index is moving down until at out of the stack size as popping or at default, indicates the stack is empty
            return True
        else:
            return False

    def isEmpty2(self):
        if self.tos2 == self.TotalSize: # The pointer index is moving up until at out of the stack size as popping at default, indicates the stack is empty
            return True
        else:
            return False

        # Pick up the last pushed val
    def peek1(self):
        if self.isEmpty1() == True: # Run when the stack is Empty
            return "Stack1 is Empty. Unable to peek"
        else:
            return self.My_stack[self.tos1] # Return the value where the pointer is at now

    def peek2(self):
        if self.isEmpty2() == True:
            return "Stack2 is Empty. Unable to peek"
        else:
            return self.My_stack[self.tos2]


class Queue():
    def __init__(self, size):
        # Ensures size is not negative, zero, or odd. If so default 2
        if size % 2 != 0 or size > 0:
            size = 2

        self.size = size
        self.myStack = TwoStack(size, size)

    # Adds numbers to the first stack while it's not full
    def Enqueue(self, data):
        if not self.isFull():
            self.myStack.push1(data)

    def Dequeue(self):
        while not self.myStack.isEmpty1():
            self.myStack.push2(self.myStack.pop1())
        dataToReturn = self.myStack.pop2()
        while not self.myStack.isEmpty2():
            self.myStack.push1(self.myStack.pop2())
        return dataToReturn

    # Simply checks if stack1 is full
    def isFull(self):
        return self.myStack.isFull1()

    # Simply checks if both stacks are empty
    def isEmpty(self):
        return self.myStack.isEmpty1() and self.myStack.isEmpty2()

#TODO Write Driver/Test code below

