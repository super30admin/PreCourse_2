# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    if low < high:
        pivot = high
        lowPointer = low
        for i in range(low, high):
            if arr[i] < arr[pivot]:
                temp = arr[i]
                arr[i] = arr[lowPointer]
                arr[lowPointer] = temp
                lowPointer += 1
        temp = arr[pivot] 
        arr[pivot] = arr[lowPointer]
        arr[lowPointer] = temp
        return lowPointer       

  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex - 1)
        quickSort(arr,partitionIndex + 1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5, 3, 2,16, 13] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "), 
  
 
