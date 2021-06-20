# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# pivot is the reference for sorting. value < pivot will be on the left side and > be on the right
# pivot value is selected from the list which is able to split the list in the half
# first and last value from the list might not be a good choice if the list is already sorted 
# (won't be able to split in half) worst case O(n^2)
# after selecting the pivot, swapping the value of pivot with the 0th position of the list (or sublist during recursive call)
# initializing two pointers (x, and the other will be each item 'i' in for loop) after the pivot and comparing the value of second pointer with the pivot
# if value < pivot, two pointers are swapped (so that value < pivot will be on the left of pivot) and moved forward
# else the forward pointer is moved 
# at the end, pivot is swapped with the first pointer
# algorithm is recursively called on the left and right parts of the pivot untill the base case is called 
# and list is sorted
# best case O(n log n)

def partition(arr,low,high):
  
  
    #write your code here
    
    mid = (high+low)//2
    pivot = high
    
    # if arr[low]<arr[mid]<arr[high], then pivot = mid
    # else, if arr[low] < arr[high], then pivot = low
    # else pivot = high
    # selecting best value of pivot to divide the list in halves
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    
    elif arr[low] < arr[high]:
        pivot = low
        
    pivotVal = arr[pivot]
    
    arr[pivot], arr[low] = arr[low], arr[pivot] # swapping pivot to the first place
    x = low # first pointer
    
    for i in range(low, high+1):
        if arr[i] < pivotVal:
            x += 1
            arr[i], arr[x] = arr[x], arr[i] # swapping to the left
            
    arr[low], arr[x] = arr[x], arr[low] # swapping the pivot at arr[low] position with the pointer
    
    return x
    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:   # if more than one items to be sorted
        part = partition(arr,low,high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 

