# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # selecting last element as pivot 
    i = low - 1
    pivot = arr[high]
    
    # traversing array and placing pivot element in the correct location in sorted array
    
    for j in range(low, high):
        if (pivot >= arr[j]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if (low < high):
        ipart = partition(arr, low, high)
        quickSort(arr, low, ipart - 1)
        quickSort(arr, ipart + 1, high)
        

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " ") 
  
 
