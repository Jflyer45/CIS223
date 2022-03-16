import random

# This is the function to deal with the split up array, which is really
# just a index range
def partition(A, p, r):
    pivotValue = A[p]
    leftMark = p + 1
    rightMark = r
    done = False
    # Keeps adjusting the marks left/right until they cross and while they havn't
    # swaps the values when appropriate.
    while not done:
        while leftMark <= rightMark and A[leftMark] <= pivotValue:
            leftMark = leftMark + 1
        while A[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1
        if rightMark < leftMark:
            done = True
        else:
            leftData = A[leftMark]
            rightData = A[rightMark]
            A[leftMark] = rightData
            A[rightMark] = leftData
    # At the end we still need to swap values of index's p and rightmark
    pData = A[p]
    rightData = A[rightMark]
    A[p] = rightData
    A[rightMark] = pData
    return rightMark

# Continues to recursivly call until the array is sorted
def quickSort(arr, low, high):
    if len(arr) <= 1:
        return arr
    if low < high:
        pivotIndex = partitionRandom(arr, low, high)
        # Quick sorts both halves.
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)


def partitionRandom(arr, start, stop):
    # Doing this helps when the array is already sorted.
    # We just chose a random index within the range
    randpivot = random.randrange(start, stop)

    # We then swap the start and the random pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    # Finally call partition like normal, but now with a number swapped.
    # Pivot value later becomes A[start]
    return partition(arr, start, stop)
