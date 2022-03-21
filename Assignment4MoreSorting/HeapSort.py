from Sort import getAscendingArray, getDecendingArray, getUnsortedArray
import sys

#Sungjae

# Building Max Heap
def MaxHeapify(Array, i, SizeofArray):
    Largest = i # Set index i as a largest
    LeftChild = int((i * 2) + 1)
    RightChild = int((i * 2) + 2)

    # Switching the potiner of largest
    if LeftChild < SizeofArray and Array[Largest] <= Array[LeftChild]:
        Largest = LeftChild
    
    if RightChild < SizeofArray and Array[Largest] <= Array[RightChild]:
        Largest = RightChild
    
    # If there was a change, swap the value
    if Largest != i:
        Array[i], Array[Largest] = Array[Largest], Array[i]

        #MaxHeapify(Array, Largest, SizeofArray) # Recursion for Maxheapifying the next level of tree
    if LeftChild < SizeofArray and RightChild < SizeofArray and Array[LeftChild] > Array[RightChild]:
        Array[LeftChild], Array[RightChild] = Array[RightChild], Array[LeftChild]    

def BuildMaxHeap(Array, sizeofArray):
    i = sizeofArray // 2 - 1 # last non-leaf node

    while i >= 0:
        MaxHeapify(Array, i, sizeofArray)
        i = i - 1

def HeapSort(Array):
    size = len(Array)
    while size > 0: # Repeating until tree has a node
        BuildMaxHeap(Array, size)
        Array[0], Array[size-1] = Array[size-1], Array[0]
        size = size - 1

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)
print(sys.getrecursionlimit())

A = getAscendingArray(100000)
print('Finish Getting Array')
HeapSort(A)
#print(A)
