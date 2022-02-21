# Written by Jeremy Fischer, Nate Bursch, Sungjae Oh

# Problem 1
def insertionSort(array, isAscendingOrder):
    for i in range(1, len(array)):
        currentNumber = array[i]
        j = i - 1

        if isAscendingOrder:
            while j >= 0 and currentNumber < array[j]:
                # Swap
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = currentNumber
        else:
            while j >= 0 and currentNumber > array[j]:
                # Swap
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = currentNumber


# Problem 2
def mergeSort(array):
    print(array)

# Problem 3
def countingSort(array):
    print(array)