import math
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