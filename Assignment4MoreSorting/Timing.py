import time, random, sys
from Assignment4MoreSorting.Sort import *

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
sys.setrecursionlimit(20000)

test = getAscendingArray(100_000)
t = time.process_time()
sortedArray = quickSort(test, 0, len(test)-1)
elapsed_time = time.process_time() - t

print(test)
print("Time: " + str(elapsed_time))
print("Is sorted: " + str(checkIfArrayIsSortedAscending(test)))