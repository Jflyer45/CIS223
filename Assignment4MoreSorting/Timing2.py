import time, sys
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

def checkIfArrayIsSortedAscending(array):

    for i in range(len(array) - 1):
        if array[i] < array[i+1] or array[i] == array[i+1]:
            continue
        else:
            return False
    return True

# We must allow the system to do more recursive calls for quick sort
sys.setrecursionlimit(10000)
test = getAscendingArray(10000)
t = time.process_time()
sortedArray = quickSort(test, 0, len(test)-1, False)
elapsed_time = time.process_time() - t

print("Elapsed Time: " + str(elapsed_time))