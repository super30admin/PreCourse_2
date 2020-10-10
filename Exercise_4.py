# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(right)
        mergeSort(left)
        len_left = len(left)
        len_right = len(right)
        i = j = k = 0
        while i < len_left and j < len_right:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len_left:
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len_right:
            arr[k] = right[j]
            k += 1
            j += 1

    # write your code here


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    # write your code here


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr) 
