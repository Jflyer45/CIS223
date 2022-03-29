from Search import *
import time, sys

def getAscendingArray(size):
    array = []
    for i in range(size):
        # Starts at 1 now
        array.append(i+1)
    return array

def testingTime(size, target, mode):
    test = getAscendingArray(size)
    times = []
    for i in range(1, 4):
        t = time.process_time()
        if mode.lower() == "l":
            print(linearSearch(test, target))
        else:
            print(BinarySearch(test, target))
        elapsed_time = time.process_time() - t
        times.append(elapsed_time)
    for i in times:
        print(i)
    print("Average: " + str((times[0]+times[1]+times[2])/3))

# testingTime(100_000, 2, "2")

print(OrderStatistic(getAscendingArray(1000), 50))