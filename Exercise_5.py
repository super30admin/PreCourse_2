# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    #write your code here
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] < pivot:
            i=i+1
            arr[i],arr[j] =arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return (i+1)

def quickSortIterative(arr, low, high):
    #write your code here
    size = len(arr)
    stack = [0] * size
    top = -1

    top = top+1
    stack[top] = low
    top = top+1
    stack[top] = high

    while top >= 0:

        high = stack[top]
        top = top-1
        low = stack[top]
        top = top-1

        piv = partition(arr,low,high)

        if piv-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = piv - 1

        if piv+1 < high:
            top = top+1
            stack[top] = piv+1
            top =top+1
            stack[top] = high
            
            
# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print (arr[i], end= " ")

