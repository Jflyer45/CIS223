class TwoStack:
    def __init__(self, size1, size2):
        self.size1 = size1
        self.size2 = size2
        self.TotalSize = size1 + size2
        self.My_stack = [None] * self.TotalSize
        self.tos1 = -1
        self.tos2 = self.TotalSize
    
    def push1(self, key): 
        if self.tos1 + 1 == self.size1:
            return False
        
        else:
            self.tos1 += 1
            self.My_stack[self.tos1] = key
            return True
    
    def push2(self, key):
        if self.tos2 == self.size1:
            return False
        
        else:
            self.tos2 -= 1
            self.My_stack[self.tos2] = key
            return True
    
    def pop1(self):
        if self.tos1 != -1:
            v = self.My_stack[self.tos1]
            self.My_stack[self.tos1] = None
            self.tos1 -= 1
            return v
        
        else:
            return False

    def pop2(self):
        if self.tos2 != self.TotalSize:
            v = self.My_stack[self.tos2]
            self.My_stack[self.tos2] = None
            self.tos2 += 1
            return v
        
        else:
            return False
            
    def isFull1(self):
        if self.tos1 >= self.size1 -1 :
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


hi = TwoStack(1, 3)

print(f"\n Check if Stack 2 is Empty: {hi.isEmpty2()}")

print(f"\nPushing 100: {hi.push2(100)}")
print(f"\nPushing 200: {hi.push2(200)}")
print(f"\n Check if Full: {hi.isFull2()}")
print(f"\n Check if Stack 2 is Empty: {hi.isEmpty2()}")
print(f"\n Peek Stack1: {hi.peek1()}")
print(f"\n Peek Stack2: {hi.peek2()}")


print(f"\nPushing 300: {hi.push2(300)}")
print(f"\nPushing 400: {hi.push2(400)}")
print(f"\n Check if Stack 2 is Empty: {hi.isEmpty2()}")



print(f"\n Check if Stack2 Full: {hi.isFull2()}")
print(f"\nPushing 400: {hi.push2(400)}")
print(f"\n Check if Stack 2 is Empty: {hi.isEmpty2()}")

print(f"Pushing 20 To Stack 1: {hi.push1(20)}")
print(f"\n Check if Stack 1 is Empty: {hi.isEmpty1()}")

print(f"Pushing 30 To Stack 1: {hi.push1(30)}")
print(f"\n Check if Stack 1 is Empty: {hi.isEmpty1()}")


print(f"\n Check if Stack 1 is Full: {hi.isFull1()}")

print(f"\nPop Stack1: {hi.pop1()}")
print(f"\nPop Stack1: {hi.pop1()}")
print(f"\nPop Stack2: {hi.pop2()}")
print(f"\nPop Stack2: {hi.pop2()}")
print(f"\nPop Stack2: {hi.pop2()}")
print(f"\nPop Stack2: {hi.pop2()}")

print(f"\n Check if Stack 1 is Empty: {hi.isEmpty1()}")










