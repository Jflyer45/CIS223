from .Problem1 import TwoStack
# TwoStack Testing
testCase = TwoStack(2, 3)

testCase.Push1(1)
testCase.Push1(2)

testCase.Push2(3)
testCase.Push2(4)
testCase.Push2(5)
# testCase.Push2(466)
# testCase.Push2(13241234)

print(testCase.array)