import BST, Node

def inorder(node):
    if node: # if the tree is not NULL
        inorder(node.getleft()) # Traverse the left subtree
        print(node.getValue(), end=" ") # Print the current node
        inorder(node.getright()) # Traverse the right subtree

#TODO Part 3