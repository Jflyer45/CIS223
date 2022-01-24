# Writen By: Jeremy Fischer, , and


class TwoStack():

    def __init__(self, size1, size2):
        # Variables
        self.size1 = size1
        self.size2 = size2
        self.array = [None] * (size1 + size2)
        self.head1 = 0
        self.head2 = len(self.array)-1

        self.stack1IsFull = False


    def Push1(self, key):
        # If the final slot is not taken, fill it in with data
        if self.stack1IsFull:
            self.array[self.head1] = key
            if(self.head1 != self.size1-1):
                self.head1 += 1
            else:
                self.stack1IsFull = True

    def Push2(self, key):
        # If the final slot is not taken, fill it in with data

        self.array[self.head2] = key
        if(self.head2 != len(self.array) - self.size2):
            self.head2 -= 1

    def Pop1(self):

        poppedValue = self.array[self.head1]
        if(self.head1 != 0):
            self.head1 -= 1
        return poppedValue

    def Pop2(self):
        poppedValue = self.array[self.head2]
        if (self.head2 != len(self.array) - 1):
            self.head2 += 1
        return poppedValue

    def Peek1(self):
        return self.array[self.head1]

    def Peek2(self):
        return self.array[self.head2]

    def isFull1(self):
        if self.head1 == self.size1-1:
            return False
        else:
            return True

    def isFull2(self):
        if self.head2 == self.size1:
            return False
        else:
            return True

    def isEmpty1(self):
        if self.head1 == 0:
            return True
        else:
            return False

    def isEmpty2(self):
        topIndex = len(self.array)-1
        if self.head2 == topIndex:
            return True
        else:
            return False
