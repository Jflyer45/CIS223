import math, random

# Task 1
def linearSearch(A, key):
    doesExist = False
    for item in A:
        if item == key:
            doesExist = True
            break
    return doesExist

# Task 2
def BinarySearch(A, key):
    found = False
    start = 1
    end = len(A)

    #as long as the lowest number is not above end and the number has not been found, start the search
    while (start <= end) and (not found):
        #get the mid point - will always be the smaller
        midpointIndex = math.floor((start+end)/2)
       
        #if the midpoint is eqaul to the key
        if A[midpointIndex] == key:
            found = True
            #this will break the while loop
        #if the keyt is not equal then it is either bigger or smaller
        else:
            #if the key is smaller than the midpoint we go to the left side
            if key < A[midpointIndex]:
                #we then know that our end is going to be one ot the left of the midpoint
                end = midpointIndex - 1
            #if the key is larger than the midpoint, we know our start value is to the right of the midpoint
            else:
                start = midpointIndex + 1
    return found

# Task 3
def OrderStatistic(A, n):
    pass

def randomizedSelect(A,p,r,i):
    if p == r:
        return A[p]
    q = randomizedPartition(A,p,r)
    k = q - p + 1
    if i==k:
        return A[q]
    elif i<k:
        return randomizedSelect(A,p,q -1, i)
    else: 
        return randomizedSelect(A, q + 1, r, i-k)

def randomizedPartition(arr, start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

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