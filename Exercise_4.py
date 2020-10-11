# Python program for implementation of MergeSort
def merge(left, right, arr):
    nL = len(left)
    nR = len(right)
    i = j = k = 0
    while i < nL and j < nR:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    while i < nL:
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < nR:
        arr[k] = right[j]
        j = j + 1
        k = k + 1

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)

# Code to print the list
def printList(arr):
    for i in arr:
        print(i)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
