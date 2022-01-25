# Writen By: Jeremy Fischer, Nate Bursch , and

# write a class called two stack: use a list to implement two stacks

class TwoStack:

    # variables shared by all two stacks
    # none

    # variables in stacks
    def __init__(self, size1, size2):
        self.max1 = size1
        self.max2 = size2
        self.stacks = []  # creates a new list for each twostack
        self.pointer = 0  # pointer starts at 0

    # methods
    def Push1(self, key):
        # check to see if the list is full
        if (self.isFull1()):  # checking to see if the list is full before adding to it
            print(f"Push 1: Not Allowed {key}")
        else:
            self.stacks.insert(self.pointer, key)
            self.pointer += 1
            # because we are pushing to stack 1 we increse the pointer. by inserting, the list automatically pushes stack two

    def Push2(self, key):
        if (self.isFull2()):  # checking to see if the list is full before adding to it
            print(f"Push 2: Not Allowed {key}")
        else:
            self.stacks.insert(self.pointer, key)
            # we do not need to change the pointer because value was added to stack two

    def Pop1(self):
        valueToReturn = self.stacks.pop(
            self.pointer - 1)  # -1 becuase the pointer is currently pointing at stack two's first value:
        self.pointer -= 1  # decreasing pointer because we took from stack 1
        return valueToReturn  # returns the popped value;

    def Pop2(self):
        if (not self.isEmpty2()):
            valueToReturn = self.stacks.pop(self.pointer)  # pointer is already on the top item in the stack
            # don't need to mess with the pointer becuase it will still be on the top list of the stack
            return valueToReturn
        else: return "Stack is Empty"

    def Peek1(self):
        return self.stacks[
            self.pointer - 1]  # return the valyue that is one under pointer. pointer rests on first value stack 2

    def Peek2(self):
        return self.stacks[self.pointer]  # pointer is on value 2

    def isFull1(self):
        # list one is full if the pointer is  > maxsize
        if (self.pointer >= self.max1):
            return True
        else:
            return False

    def isFull2(self):
        if (len(self.stacks) - self.pointer >= self.max2):
            return True
        else:
            return False

    def isEmpty1(self):
        
        if (self.pointer == 0):
            return True
        else:
            False

    def isEmpty2(self):
        if (len(self.stacks) == self.pointer):
            return True
        else:
            False