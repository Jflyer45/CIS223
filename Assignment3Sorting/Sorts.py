# Written by Jeremy Fischer, Nate Bursch, Sungjae Oh
import time, random
# Problem 1 Jeremy Fischer
# Code is based off class code from slides
def insertionSort(array, isAscendingOrder):
    for i in range(1, len(array)):
        currentNumber = array[i]
        j = i - 1

        # If ascending currentNumber < array[j]
        if isAscendingOrder:
            while j >= 0 and currentNumber < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = currentNumber
        # Else sort by descending by currentNumber > array[j]
        else:
            while j >= 0 and currentNumber > array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = currentNumber


# Problem 2

def MergeSort(A):

    if len(A) <= 1:
        print("Returning original Array ............")
        print(A)
        return A

    else:
        print("DIVIDING INTO TWO ARRAYS ............")
        midPoint = len(A)//2
        L = A[:midPoint]
        R = A[midPoint:len(A)]

        print("Recursion for L")
        L = MergeSort(L)
        print("Recursion for R")
        R = MergeSort(R)

        print("RETURNING MERGED ARRAY...")
        return MergeArrays(L, R)

def MergeArrays(L, R):
        #Sorting by using pointer
        print("Defining pointer...")
        lp = 0 # left pointer
        rp = 0 # right pointer
        mp = 0 # pointer for merged array
        size = len(L) + len(R)
        SortedArray = [None] * size # Assigning the size of array

        while lp < len(L) and rp < len(R):
            if L[lp] < R[rp]:
                SortedArray[mp] = L[lp]
                lp += 1
                mp += 1
            else:
                SortedArray[mp] = R[rp]
                rp += 1
                mp += 1

        # Assigning values in the rest of the array
        if lp >= len(L):
            while rp < len(R):
                SortedArray[mp] = R[rp]
                rp += 1
                mp += 1

        elif rp >= len(R):
            while lp < len(L):
                SortedArray[mp] = L[lp]
                lp += 1
                mp += 1

        print("Returning Sorted Array .....")
        print(SortedArray)
        return SortedArray



# Problem 3
# Nate Bursch
#O(n+k)
#k is the max number in the array
#O(k) - stable sorting algorithm, the order of two numbers that are the same, is preserved.
def countingSort(arraytoCount,maxNumber):

    #this will just create the values to be 0, so no need to have the first loop
    ArrayCount = [0] * int(maxNumber+1)
    sortedArrayB = [None] * int(maxNumber+1)
    

    #second loop count the number of occurance
    for j in range(1,len(arraytoCount)):
        #so now at index j, the value is increased by one for every time the index is scene in arraytocount
        ArrayCount[arraytoCount[j]] = ArrayCount[arraytoCount[j]]+1



    #third loop adds all the values up in a running sum. index 1 = 1, index 2 = 3 and now its 4 because it adds one.
    for i in range(1,maxNumber+1):
        ArrayCount[i] = ArrayCount[i] + ArrayCount[i-1]

    #fourth loop, place each element of counting array to the corrected sorratec position
    for j in range(len(arraytoCount)-1,1,-1):
        
        sortedArrayB[ArrayCount[arraytoCount[j]]] = arraytoCount[j]
        ArrayCount[arraytoCount[j]] = ArrayCount[arraytoCount[j]]-1
    
    return sortedArrayB



def getUnsortedArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(1, 10000))
    return array

def checkIfArrayIsSortedAscending(array):
    for i in range(len(array) - 1):
        if array[i] < array[i+1] or array[i] == array[i+1]:
            continue
        else:
            return False
    return True

size = 10000
test = getUnsortedArray(size)
t = time.process_time()
sortedArray = countingSort(test,10000)
elapsed_time = time.process_time() - t

print(sortedArray)
print(elapsed_time)