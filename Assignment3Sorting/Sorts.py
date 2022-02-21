# Written by Jeremy Fischer, Nate Bursch, Sungjae Oh

# Problem 1
def insertionSort(array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):

        key = array[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Problem 2
def mergeSort(array):
    print(array)

# Problem 3
def countingSort(array):
    print(array)