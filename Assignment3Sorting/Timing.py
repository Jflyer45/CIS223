import time, random

def getUnsortedArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 1000))
    return array

t = time.process_time()
sortedArray = None # put sort here
elapsed_time = time.process_time() - t
