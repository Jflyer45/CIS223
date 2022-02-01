# This is the file we will turn to txt to turn in

class TwoStack:
    def __init__(self, size1, size2):           # accept two integer numbers to define stack's size
        self.size1 = int(size1)
        self.size2 = int(size2)
        self.TotalSize = size1 + size2          # Define Whole size of the stack
        self.My_stack = [None] * self.TotalSize # putting placeholder as many times as TotalSize
        self.tos1 = -1                          # The pointer (top of stack) of stack 1; starting the head of the stack
        self.tos2 = self.TotalSize              # The pointer (top of stack) of stack 2; starting from the end of the stack

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

    # Empty the stack1 to the stack2 and pops1. Then pops everything back to stack1
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

# test every function and the extremes
# test
# test full empy and peek twostack functions
def TestTwoStack(twostack, aString):
    string = "---------------------------------------------"
    string += "\nTesting " + aString + "\n"

    string += "\nStack 1\n"
    string += "Stack 1 Full = {}\n".format(twostack.isFull1())
    string += "Stack 1 Empty = {}\n".format(twostack.isEmpty1())
    string += "Stack 1 Peek = {}\n".format(twostack.peek1())

    string += "\nStack 2\n"
    string += "Stack 2 Full = {}\n".format(twostack.isFull2())
    string += "Stack 2 Empty = {}\n".format(twostack.isEmpty2())
    string += "Stack 2 Peek = {}\n".format(twostack.peek2())

    print(string)


# twostack

# empty
emptyStack = TwoStack(0, 0)
# does not allow anything to be pushed
emptyStack.push1(900)
emptyStack.push2(100)
# does not allow anything to be removed
emptyStack.pop1()
emptyStack.pop2()
# states the stack is full
print(emptyStack.isFull1())
print(emptyStack.isFull2())
# states the stack is also empty
print(emptyStack.isEmpty1())
print(emptyStack.isEmpty2())
# try to peek at the value #states the stack is empty unable to peek
print(emptyStack.peek1())
print(emptyStack.peek2())

# negative extreme
negativeStack = TwoStack(-5, -100)
# error says index is out of range
# negativeStack.push1(5)

# super large
# maxStack = TwoStack(999999999999999999999999,9999999999999999999999) #error

# regular
aStack = TwoStack(5, 5)
TestTwoStack(aStack, "1")  # allvalues come out how they are supposed to

aStack.push1(0)
TestTwoStack(aStack, "2")  # allvalues come out how they are supposed to

# fill the two stack
aStack.push1(1)
aStack.push1(2)
aStack.push1(3)
aStack.push1("winner")
TestTwoStack(aStack, "3")
# try to add another value
aStack.push1(5)  # get a no valid response

# stack two is filled
aStack.push2(5)
aStack.push2(6)
aStack.push2(7)
aStack.push2(8)
aStack.push2(9)
TestTwoStack(aStack, "4")
# try to ass another value
aStack.push2(10)  # get a not valid response

# remove values
print(aStack.pop1())  # should be "winner"
print(aStack.pop1())  # should be 3

TestTwoStack(aStack, "5")  # only has 012 in stack one: stack two is normal

print(aStack.pop2())  # should print 9
# check that both empty peek and full are working for both stacks, when mid full
TestTwoStack(aStack, "6")

# print current stacks
print(aStack.My_stack)

# empty out both stacks
print(aStack.pop1())  # should be 2
print(aStack.pop1())  # should be 1
print(aStack.pop1())  # should be 0
# try to pop again
print(aStack.pop1())  # should state it is empty - states'false'

print(aStack.pop2())  # should print 8
print(aStack.pop2())  # should print 7
print(aStack.pop2())  # should print 6
print(aStack.pop2())  # should print 5
# try to pop again
print(aStack.pop2())  # should print empty - prints false

TestTwoStack(aStack, "7")

# end of twostack testing
print("End of twostack test\n--------------------------")

print("*Queue Testing*")
print("-----------------------")
# Q testing
# empty q
emptyQ = Queue(0)
print(emptyQ.myStack.My_stack)  # empty
# try to add to the q
emptyQ.Enqueue(10)  # nothing happens
print(emptyQ.myStack.My_stack)  # empty

# try to dq
emptyQ.Dequeue()  # nothing happens
print(emptyQ.myStack.My_stack)  # empty

# check to see if its full / empty should be both
print(emptyQ.isEmpty())
print(emptyQ.isFull())
print("-----------------------")

# create a q with negative values
negativeQ = Queue(-10)
print(negativeQ.myStack.My_stack)  # has an empty q

# try to add to negQ
negativeQ.Enqueue(1000)  # nothing happens
print(negativeQ.myStack.My_stack)  # has an empty q
negativeQ.Dequeue()  # nothing happens

print(negativeQ.isEmpty())
print(negativeQ.isFull())
print("-----------------------")

# create a large value q
# maxQ = Queue(9000000)#any bigger I get a memory error, youll have to trust me when I say this works.
# print(maxQ.myStack.My_stack)  #now has only 2 positions because the number is so large it doesn't have a value. so it defaults to size two.

# maxQ.Enqueue(0)
# maxQ.Enqueue(1)# seems like it is full
# maxQ.Enqueue(2)
# maxQ.Enqueue(3)
# maxQ.Enqueue(4) #none of these values were added
# print(maxQ.myStack.My_stack)  #now has only 2 positions

# print(maxQ.isFull()) #this is true
# print(maxQ.isEmpty()) # this is false

# try to dq
# print(maxQ.Dequeue()) # should be 0

# print(maxQ.isFull()) #this is false
# print(maxQ.isEmpty()) # this is false

# try to add another after dqing
# maxQ.Enqueue(2)
# print(maxQ.myStack.My_stack)  #now has only 2 positions 1,2
# print(maxQ.Dequeue()) # should be 1
# print(maxQ.Dequeue()) # should be 2

# print(maxQ.isFull()) #this is false
# print(maxQ.isEmpty()) # this is true
# end of max q testing
print("-----------------------")

# normal q test large amount
bigq = Queue(100)
print(bigq.myStack.My_stack)

# fill the q up last number will be 99
number = 0
while (not bigq.isFull()):
    bigq.Enqueue(number)
    number += 1
print("full Q ------------------")
print(bigq.myStack.My_stack)
print("--------------------------")

# now we will print each number until it is empty
string = ""
while (not bigq.isEmpty()):
    string += "{} ".format(bigq.Dequeue())
print(string)
# it prints in order starting at 0
print("--------------------------")
print("End of testing")