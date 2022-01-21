# Writen By: Jeremy Fischer, , and
from Problem1 import TwoStack

testCase = TwoStack(2, 3)

testCase.Push1(1)
testCase.Push1(2)

testCase.Push2(5)
testCase.Push2(4)
testCase.Push2(4)
testCase.Push2(466)
testCase.Push2(13241234)
print(testCase.head2)

print(testCase.array)

print(testCase.isFull1())
print(testCase.isFull2())



