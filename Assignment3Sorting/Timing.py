import time, random
from Assignment3Sorting.Sorts import *
# from Sorts import *


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

#test = getUnsortedArray(1000_000)

# Test for Ascending Order Array
# For size of 10000


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
TestFunction(10000, "M")
TestFunction(100000, "M")
TestFunction(1000000, "M")



# testd = getDecendingArray(1000000)
# t = time.process_time()
# sortedArray = MergeSort(testd)
# elapsed_time = time.process_time() - t

# print("\n****RESULT****")
# print(elapsed_time)
# print(checkIfArrayIsSortedAscending(sortedArray))
