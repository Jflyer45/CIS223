def partition(arr, low, high, isOrderAscending):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if isOrderAscending:
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] >= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high, isOrderAscending):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        if isOrderAscending:
            pi = partition(arr, low, high, True)
            quickSort(arr, low, pi - 1, True)
            quickSort(arr, pi + 1, high, True)
        else:
            pi = partition(arr, low, high, False)
            quickSort(arr, low, pi - 1, False)
            quickSort(arr, pi + 1, high, False)