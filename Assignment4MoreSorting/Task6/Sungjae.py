class node:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.value = key

    def getValue(self):
        return self.value

    def setValue(self, node):
        self.value = node.value

    def getLeft(self):
        return self.left_child
    
    def setLeft(self, node):
        self.left_child = node
    
    def getRight(self):
        return self.right_child

    def setRight(self, node):
        self.right_child = node

    

class BST:
    def __init__(self):
        self.root = None

    def searchNode(self, key):
        temp = self.root
        IsFound = False
        
        while temp != None:
            if node.value < temp.value:
                temp = temp.left_child
            elif node.value > temp.value:
                temp = temp.right_child
            elif node.value == temp.value:
                IsFound = True
                break
        
        if IsFound == False:
            return print("Not Found"), False
        else:
            return print("Found"), True, temp

    def insertNode(self, node):

        if self.root == None:
            self.root = node
        
        else:

            temp = self.root
            
            while temp.right_child and temp.left_child != None:
                if node.value < temp.value:
                    temp = temp.left_child
                else:
                    temp = temp.right_child
                
            if node.value < temp.value:
                temp.setLeft(node)
            else:
                temp.setRight(node)
            
            return True
    
    def deleteNode(self, key):
        if BST.searchNode(key) == True: 
            BST.searchNode(key).temp = None
            print("Deleted")
            return True
        else:
            print("Given value is not Found")


if __name__ == "__main__":
    n1 = node(2)
    n2 = node(1)
    n3 = node(3)
    n4 = node(2)
    n5 = node(7)
    print(n1.getValue())
    Tree = BST()
    Tree.insertNode(n1)
    Tree.insertNode(n2)
    Tree.insertNode(n3)
    Tree.insertNode(n4)
    Tree.insertNode(n5)

    print('searching node 5...')
    Tree.searchNode(5)

    print('searching node 1...')
    Tree.searchNode(1)

    print('deleting node 1....')
    Tree.deleteNode(1)

    print('searching node 1 again...')
    Tree.searchNode(1)

    print("PROGRAM DONE")










