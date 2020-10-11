# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    pIndex = low
    for i in range(low, high):
        if(arr[i] <= pivot):
            arr[i], arr[pIndex] =  arr[pIndex], arr[i]
            pIndex = pIndex + 1
    arr[pIndex], arr[high] = arr[high], arr[pIndex]
    return pIndex
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if(low<high):
        pIndex = partition(arr, low, high)
        quicksort(arr, low, pIndex-1)
        quicksort(arr, pIndex+1, high)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
