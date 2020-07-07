# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# This function selects the last element of the array as the pivot. It then places the pivot in 
# correct position in array and moves all less than pivot elements to the left of pivot
# and all greater than pivot elements to the right of pivot
def partition(arr,low,high):
    #write your code here
    l = low-1
    pivot = arr[high]
    for k in range(low, high):
        if arr[k]<=pivot:
            l +=1
            arr[l],arr[k] = arr[k], arr[l]
    arr[l+1],arr[high] = arr[high], arr[l+1]
    return l+1


# Function to do Quick sort recursively
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        pos = partition(arr,low,high)
        quickSort(arr,low,pos-1)
        quickSort(arr,pos+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
