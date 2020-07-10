# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot_element = arr[high]
    slow_ptr = low
    fast_ptr = low

    while fast_ptr < high:
        if arr[fast_ptr] < pivot_element:
            arr[slow_ptr], arr[fast_ptr] = arr[fast_ptr], arr[slow_ptr]
            slow_ptr +=1
        fast_ptr +=1

    arr[slow_ptr], arr[high] = arr[high], arr[slow_ptr]

    return slow_ptr


# Function to do Quick sort
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:

        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
