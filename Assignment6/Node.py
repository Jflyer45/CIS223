# Problem 1
class Node:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.value = key
    # Part a
    def getValue(self):
        return self.value
    # Part b
    def setValue(self, data):
        self.value = data
    # Part c
    def getLeft(self):
        return self.left_child
    # Part D
    def setLeft(self, data):
        self.left_child.setValue(data)
    # Part E
    def getRight(self):
        return self.right_child
    # Part F
    def setRight(self, data):
        self.left_child.setValue(data)