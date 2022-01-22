# Writen By: Jeremy Fischer, Nate Bursch, and

class TwoStack():
    def __init__(self, size1, size2):
        # Variables
        self.size1 = size1
        self.size2 = size2
        self.array = [None] * (size1 + size2)
        self.head1 = 0
        self.head2 = len(self.array)-1

    def Push1(self, key):
        # If the final slot is not taken, fill it in with data
        if(self.array[self.size1-1] is None):
            self.array[self.head1] = key
            if(self.head1 != self.size1-1):
                self.head1 += 1

    def Push2(self, key):
        # If the final slot is not taken, fill it in with data
        # print()
        if(self.array[len(self.array) - self.size2] is None):
            print("this happend")
            self.array[self.head2] = key
            if(self.head2 != len(self.array) - self.size2):
                self.head2 -= 1

    def Pop1(self):
        # TODO what if pop at index 1 where it is null
        poppedValue = self.array[self.head1]
        self.array[self.head1] = None
        if(self.head1 != 0):
            self.head1 -= 1
        return poppedValue

    def Pop2(self):
        poppedValue = self.array[self.head2]
        self.array[self.head2] = None
        if (self.head2 != len(self.array) - 1):
            self.head2 += 1
        return poppedValue

    def Peek1(self):
        return self.array[self.head1]

    def Peek2(self):
        return self.array[self.head2]

    def isFull1(self):
        if(self.array[self.size1 - 1] is None):
            return False
        else:
            return True

    def isFull2(self):
        if (self.array[len(self.array) - self.size2] is None):
            return False
        else:
            return True

    def isEmpty1(self):
        if(self.head1 == 0 and self.array[0] is None):
            return True
        else:
            return False

    def isEmpty2(self):
        topIndex = len(self.array)-1
        if (self.head2 == topIndex and self.array[topIndex] is None):
            return True
        else:
            return False


class QUEUE:
    def __init__(self, max):
        self.max = max
        self.eq_counter = 0 #this allows us to not rely on the stacks pointer
        self.dq_counter = 0
        self.stackClass = TwoStack(max/2,max/2)
    def Enqueue(self,key):
        if(not(self.isFull())): #check to see if the queue is full
            if(self.isEven()): # if the counter is on an even number we push to the first stack.
                self.stackClass.Push1(key)
                self.counter += 1
            else:                           #else ^the pointer is odd^ we push to the second stack.
                self.stackClass.Push2(key)
                self.counter += 1 #adding to the q adds to the counter
        else:
            print(f"Not allowed to Queue {key}") #if q is full print this statement*it can be whatever