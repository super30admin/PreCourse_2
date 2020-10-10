# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr, low, high):
    end = high
    swaper_index = low
    for i in range(low, high):
        if arr[i] < arr[high]:
            arr[swaper_index], arr[i] = arr[i], arr[swaper_index]
            swaper_index += 1
    arr[swaper_index], arr[high] = arr[high], arr[swaper_index]
    return swaper_index

    # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

    # write your code here


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


