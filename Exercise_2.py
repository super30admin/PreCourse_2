# Python program for implementation of Quicksort Sort 
  
def partition(arr,low,high):
    #  take the last element as pivot and
    #  place the elements less than pivot on left side and
    #  all elements greater than pivot on right side of it in the array
    pivot = arr[high]
    #lets say index of smallest element be low-1
    k = low -1
    for j in range(low, high):
        if arr[j]<pivot:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]
        # print(arr)
    arr[k+1], arr[high] = arr[high], arr[k+1]
    return (k+1)  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr,low,p-1)
        quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

"""
Quick sort has O(nlogn) complexity in the best case where median element is selected as pivot.
it has O(n^2) complexity when smallest or largest element is picked as pivot.
"""
  
 
