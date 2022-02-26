import time, random
from Sorts import *

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

test = getUnsortedArray(100)
t = time.process_time()
sortedArray = MergeSort(test)
elapsed_time = time.process_time() - t

print("\n****RESULT****")
print(elapsed_time)
print(checkIfArrayIsSortedAscending(sortedArray))
