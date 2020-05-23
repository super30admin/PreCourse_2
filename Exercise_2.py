# Python program for implementation of Quicksort Sort   
# give you explanation for the approach

# Time: O(nlog n) | Time: O(nlog n ) , where n is the number of elements of the array.
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low,high):
        if arr[j] < pivot :
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    
    if low < high:
        partition_index = partition(arr,low,high)
        quickSort(arr,low,partition_index-1)
        quickSort(arr,partition_index+1,high)
        

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
