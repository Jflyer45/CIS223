import random,time

# This is the function to deal with the split up array, which is really
# just a index range
def partition(A, p, r):
    pivotValue = A[p]
    leftMark = p + 1
    rightMark = r
    done = False
    # Keeps adjusting the marks left/right until they cross and while they havn't
    # swaps the values when appropriate.
    while not done:
        while leftMark <= rightMark and A[leftMark] <= pivotValue:
            leftMark = leftMark + 1
        while A[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1
        if rightMark < leftMark:
            done = True
        else:
            leftData = A[leftMark]
            rightData = A[rightMark]
            A[leftMark] = rightData
            A[rightMark] = leftData
    # At the end we still need to swap values of index's p and rightmark
    pData = A[p]
    rightData = A[rightMark]
    A[p] = rightData
    A[rightMark] = pData
    return rightMark

# Continues to recursivly call until the array is sorted
def quickSort(arr, low, high):
    if len(arr) <= 1:
        return arr
    if low < high:
        pivotIndex = partitionRandom(arr, low, high)
        # Quick sorts both halves.
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)


def partitionRandom(arr, start, stop):
    # Doing this helps when the array is already sorted.
    # We just chose a random index within the range
    randpivot = random.randrange(start, stop)

    # We then swap the start and the random pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    # Finally call partition like normal, but now with a number swapped.
    # Pivot value later becomes A[start]
    return partition(arr, start, stop)



#Nates Part
def radixSort(array):
    #create ten buckets related the the base amount of integers 0-9
    #O(nw) w is the length of the longest digit, very fast for lots of data, super slow for small data with large digits
    #get max amount of digits
    maxDigits = len(str(max(array)))
    #now do the radix sort
    #this is starting the bucket list
    for digit in range(0,maxDigits):
        #create the buckets 0-9 = 10
        buckets = [[] for i in range(10)]
        #now we can cycle through
        #constant exponent for each number, cut time in almost half
        e = 10**digit
        for number in array:
            #this gets the right most digit so we know what bucket to put the number in
            bucketNumber = number // e % 10
            #add the number to the bucket
            buckets[bucketNumber].append(number)
        #now we need to flatten
        array = []
        for bucket in buckets:
            for number in bucket:
                array.append(number)
    return array



#Sungjae
# Heap Sort
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

        MaxHeapify(Array, Largest, SizeofArray) # Recursion for Maxheapifying the next level of tree

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




#timing and other stuff
def getAscendingArray(size):
    array = []
    for i in range(size):
        array.append(i)
    return array

def getDecendingArray(size):
    array = []
    i = size
    while i >= 1:
        array.append(i)
        i -= 1
    return array

def getUnsortedArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 1000))
    return array

def checkIfArrayIsSortedAscending(array):

    for i in range(len(array) - 1):
        if array[i] < array[i+1] or array[i] == array[i+1]:
            continue
        else:
            return False
    return True

# We must allow the system to do more recursive calls for quick sort


def TestFunction(Size, Method):
    S = Size
    if Method == "R":
        sorting = "Radix Sort"
    elif Method == "Q":
        sorting = "Quick sort"
    elif Method == "H":
        sorting = "Heap sort"
    print(f"\nStart the testing for Size <{S}> array with <{sorting}>")
    Result = []

    if Method == "R":
        for i in range(3):
            print(f'Trial {i+1} for Ascending Array')
            test = getAscendingArray(S)
            t = time.process_time()
            sortedArray = radixSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
            

        for i in range(3):
            print(f'Trial {i+1} for Desceding Array')
            test = getDecendingArray(S)
            t = time.process_time()
            sortedArray = radixSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
    
    Sum = 0
    for T in Result:
        Sum += T
    Avg = Sum / len(Result)

    print(f"Result\n {Result}")
    print(f' Avg Time: {Avg}')

    print("\n***** TEST COMPLETED *****")


# Method Selction: I-> Insertion Sort /// C -> Counting Sort /// M -> Merge Sort
TestFunction(10000, "R")
TestFunction(100000, "R")
TestFunction(1000000, "R")