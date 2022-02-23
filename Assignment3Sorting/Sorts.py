# Written by Jeremy Fischer, Nate Bursch, Sungjae Oh

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
def mergeSort(array):
    print(array)

# Problem 3
# Nate Bursch
#O(n+k)
#k is the max number in the array
#O(k) - stable sorting algorithm, the order of two numbers that are the same, is preserved.
def countingSort(arraytoCount,max):
    ArrayCount = [None] * max
    sortedArrayB = [] 
    for i in range(max):
        #set all values to 0
        ArrayCount[i] = 0
    #second loop count the number of occurances
    for j in range(1,arraytoCount.length):
        #so now at index j, the value is increased by one for every time the index is scene in arraytocount 
        ArrayCount[arraytoCount[j]] = ArrayCount[arraytoCount[j]]+1
    
    #third loop adds all the values up in a running sum. index 1 = 1, index 2 = 3 and now its 4 because it adds one.
    for l in range(1,max):
        ArrayCount[l] = ArrayCount[l] + ArrayCount[l-1]
    
    #fourth loop, place each element of counting array to the corrected sorratec position
    for m in range(arraytoCount.length,1,-1):
        sortedArrayB[ArrayCount[m]] = arraytoCount[m]
        ArrayCount[arraytoCount[m]] = ArrayCount[arraytoCount[m]] - 1



    print(sortedArrayB)