# Writen By: Jeremy Fischer, Nate Bursch , and

#write a class called two stack: use a list to implement two stacks

class TWOSTACK:

    #variables shared by all two stacks
    #none

    #variables in stacks
    def __init__(self, size1, size2):
        self.max1 = size1
        self.max2 = size2
        self.stacks = [] #creates a new list for each twostack
        self.pointer = 0 #pointer starts at 0
    
    #methods
    def Push1(self,key):
        #check to see if the list is full
        if(self.isFull1): #checking to see if the list is full before adding to it
            self.stacks.insert(self.pointer,key)
            self.pointer += 1
        else:
            print("Not Allowed")
            #because we are pushing to stack 1 we increse the pointer. by inserting, the list automatically pushes stack two

    def Push2(self,key):
        self.stacks.insert(self.pointer,key)
        #we do not need to change the pointer because value was added to stack two


    def Pop1(self):
        valueToReturn = self.stacks.pop(self.pointer-1) # -1 becuase the pointer is currently pointing at stack two's first value:
        self.pointer -= 1 #decreasing pointer because we took from stack 1
        return valueToReturn #returns the popped value;

    def Pop1(self):
        self.stacks.pop()

    def isFull1(self):
        #list one is full if the pointer is  > maxsize
        if(self.pointer < self.max1):
            return True
        else: return False
        

    def isFull2(self):
        if(len(self.stacks)== self.size1):
            return True
        else: False

    def isEmpty1(self):
        if(len(self.stacks)==0):
            return True
        else: False

    def isEmpty1(self):
        if(len(self.stacks)==0):
            return True
        else: False


butt = TWOSTACK(5,5)
maxStack1 = butt.max1
maxStack2 = butt.max2


butt.Push1(0)
butt.Push1(1)
butt.Push1(2)
butt.Push1(2)
butt.Push1(2)
butt.Push1(2)
butt.Push1(2)
butt.Push1(2)







butt.Push2(3)
butt.Push2(4)
butt.Push2(5)



stack1full = butt.isFull1()

print(butt.stacks)

        