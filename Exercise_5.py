# Python program for implementation of Quicksort

from collections import deque

def partition(arr, l, h):

    pivot = arr[h]
    pIndex = l
    for i in range(l, h):
        if arr[i] <= pivot:
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
            pIndex = pIndex + 1

    arr[pIndex], arr[h] = arr[h], arr[pIndex]
    return pIndex


def quickSortIterative(arr, l, h):

    stack = deque()
    stack.append((l, h))
    while stack:
        l, h = stack.pop()

        pivot = partition(arr, l, h)
        if pivot - 1 > l:
            stack.append((l, pivot - 1))
        if pivot + 1 < h:
            stack.append((pivot + 1, h))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is: ")
for i in range(n):
    print("%d" %arr[i]),