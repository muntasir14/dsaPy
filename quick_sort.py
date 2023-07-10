"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def quicksort(array):
    low = 0
    high = len(array) - 1
    quick_sort(array, low, high)

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
