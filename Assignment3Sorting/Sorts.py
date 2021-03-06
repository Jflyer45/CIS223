# Written by Jeremy Fischer, Nate Bursch, Sungjae Oh
import time, random
# Problem 1 Jeremy Fischer
# Code is based off class code from slides
def insertionSort(array):
    for i in range(1, len(array)):
        currentNumber = array[i]
        j = i - 1

        # Goes through all the numbers backwards until it finds it's correct spot
        while j >= 0 and currentNumber < array[j]:
            array[j + 1] = array[j]
            j -= 1
        # Places it at it's correct spot
        array[j + 1] = currentNumber


# Problem 2

def MergeSort(A):

    if len(A) <= 1:
        #print("Returning original Array ............")
        #print(A)
        return A

    else:
        #print("DIVIDING INTO TWO ARRAYS ............")
        midPoint = len(A)//2
        L = A[:midPoint]
        R = A[midPoint:len(A)]

        #print("Recursion for L")
        L = MergeSort(L)
        #print("Recursion for R")
        R = MergeSort(R)

        #print("RETURNING MERGED ARRAY...")
        return MergeArrays(L, R)

def MergeArrays(L, R):
        #Sorting by using pointer
        #print("Defining pointer...")
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

        #print("Returning Sorted Array .....")
        #print(SortedArray)
        return SortedArray



# Problem 3
# Nate Bursch
#O(n+k)
#k is the max number in the array
#O(k) - stable sorting algorithm, the order of two numbers that are the same, is preserved.
def countingSort(arraytoCount):
    BiggestNumber = int(max(arraytoCount)) # I feel that this number takes a very long time.

    SmallestNumber = int(min(arraytoCount)) #this will fix the error when there is a 0 number


    ArrayLength = int(len(arraytoCount))


    #this will just create the values to be 0, so no need to have the first loop
    #ArrayCount = [0] * (BiggestNumber+1) # we need to include 0 if it exists
    #changing tit to the range of elemts between smalles ant biggest, because sometimes there might not be a 0
    ArrayCount = [0] * (BiggestNumber-SmallestNumber+1)
    ArrayOutput = [None] * ArrayLength
    #'second' loop count the number of occurance
    for i in range(0,ArrayLength):
        #so now at index i, the value is increased by one for every time the index is scene in arraytocount
        ArrayCount[arraytoCount[i]-SmallestNumber] += 1
        
    #third loop adds all the values up in a running sum. index 1 = 1, index 2 = 3 and now its 4 because it adds one.
    
    for j in range(1,len(ArrayCount)):
        ArrayCount[j] = ArrayCount[j] + ArrayCount[j-1]

    #fourth loop, place each element of counting array to the corrected sorrated position
    for k in range(ArrayLength-1,-1,-1):
        ArrayOutput[ArrayCount[arraytoCount[k]-SmallestNumber]-1] = arraytoCount[k]
        ArrayCount[arraytoCount[k] - SmallestNumber] = ArrayCount[arraytoCount[k]-SmallestNumber]-1

    # else: #decensding order
        
    #     for j in range(len(ArrayCount)-2,-1,-1):
    #         ArrayCount[j] = ArrayCount[j] + ArrayCount[j+1]
    #     #fourth loop, place each element of counting array to the corrected sorrated position
        
    #     for k in range(0, ArrayLength):
    #         try:
    #             ArrayOutput[ArrayCount[arraytoCount[k]-SmallestNumber]-1] = arraytoCount[k]
    #             ArrayCount[arraytoCount[k] - SmallestNumber] = ArrayCount[arraytoCount[k]-SmallestNumber]-1
    #         except:
    #             continue


    

    return ArrayOutput

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
        array.append(random.randint(0, 100_000))
    return array

def checkIfArrayIsSortedAscending(array):
    for i in range(len(array) - 1):
        if array[i] < array[i+1] or array[i] == array[i+1]:
            continue
        else:
            return False
    return True



def TestFunction(Size, Method):
    S = Size
    if Method == "I":
        sorting = "insertion sort"
    elif Method == "C":
        sorting = "counting sort"
    elif Method == "M":
        sorting = "merge sort"
    print(f"\nStart the testing for Size <{S}> array with <{sorting}>")
    Result = []

    if Method == "I":
        for i in range(3):
            print(f'Trial {i+1} for Ascending Array')
            test = getAscendingArray(S)
            t = time.process_time()
            sortedArray = insertionSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
            

        for i in range(3):
            print(f'Trial {i+1} for Desceding Array')
            test = getDecendingArray(S)
            t = time.process_time()
            sortedArray = insertionSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
    
    elif Method == "M":
        for i in range(3):
            print(f'Trial {i+1} for Ascending Array')
            test = getAscendingArray(S)
            t = time.process_time()
            sortedArray = MergeSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
            

        for i in range(3):
            print(f'Trial {i+1} for Desceding Array')
            test = getDecendingArray(S)
            t = time.process_time()
            sortedArray = MergeSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)

    elif Method == "C":
        for i in range(3):
            print(f'Trial {i+1} for Ascending Array')
            test = getAscendingArray(S)
            t = time.process_time()
            sortedArray = countingSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
            

        for i in range(3):
            print(f'Trial {i+1} for Desceding Array')
            test = getDecendingArray(S)
            t = time.process_time()
            sortedArray = countingSort(test)
            elapsed_time = time.process_time() - t

            # print(elapsed_time)
            Result.append(elapsed_time)
        
        else: 
            print("Method should be I, M, or C")

    Sum = 0
    for T in Result:
        Sum += T
    Avg = Sum / len(Result)

    print(f"Result\n {Result}")
    print(f' Avg Time: {Avg}')

    print("\n***** TEST COMPLETED *****")


# Method Selction: I-> Insertion Sort /// C -> Counting Sort /// M -> Merge Sort
TestFunction(10000, "I")
TestFunction(100000, "I")
TestFunction(1000000, "I")
