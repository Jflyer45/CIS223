import time, random

def getUnsortedArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 1000))
    return array

def checkIfArrayIsSortedAscending(array):

    for i in range(len(array) - 1):
        if array[i] < array[i+1] or i == array[i+1]:
            continue
        else:
            return False
    return True

t = time.process_time()
sortedArray = None # put sort here
elapsed_time = time.process_time() - t
