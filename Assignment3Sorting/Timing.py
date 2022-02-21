import time, random
from Assignment3Sorting.Sorts import insertionSort


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

test = getUnsortedArray(10_000)
t = time.process_time()
sortedArray = insertionSort(test) # put sort here
elapsed_time = time.process_time() - t

print(elapsed_time)
print(checkIfArrayIsSortedAscending(test))
print(test)