import time, random
#from Assignment3Sorting.Sorts import *
from Sorts import *


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

def getRandomUnsortedList(size):
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

<<<<<<< Updated upstream
#test = getUnsortedArray(1000_000)
test = getAscendingArray(10000)
t = time.process_time()
sortedArray = MergeSort(test)
=======
def getSortedListAsc(size):
    returnList = []
    for i in range(size):
        returnList.append(i)
    return returnList

def getSortedListDesc(size):
    returnList = []
    for i in range(size):
        returnList.append(size-i)
    return returnList

test = getSortedListDesc(100_000)
t = time.process_time()
sortedArray = insertionSort(test)
>>>>>>> Stashed changes
elapsed_time = time.process_time() - t

print("\n****RESULT****")
print(elapsed_time)
# print(checkIfArrayIsSortedAscending(sortedArray))
