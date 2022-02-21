import time, random, sys
from Assignment4MoreSorting.Sort import *

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
sys.setrecursionlimit(2000)

test = getUnsortedArray(1_000)
t = time.process_time()
sortedArray = quickSort(test, 0, len(test)-1, False)
elapsed_time = time.process_time() - t

print(elapsed_time)
print(checkIfArrayIsSortedAscending(test))
print(test)