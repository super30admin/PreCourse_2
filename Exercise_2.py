# Python program for implementation of Quicksort Sort 

#swap index values
def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# give you explanation for the approach
def partition(arr,low,high):
    #take last element as pivot point (number to compare to)
    pivot = arr[high]
    
    partitionIndex = low - 1
    #traverse arr from low to high
    for i in range(low, high):
        #if current is <= than the pivot point
        if arr[i] <= pivot:
           partitionIndex += 1
           swap(arr,i, partitionIndex)
        
    #swap last element and then return partitionIndex
    swap(arr, partitionIndex+1, high)
    return partitionIndex+1
    #write your code here
  

# Function to do Quick sort..time:O(nlgn) at best O(N^2) at worse space:O(lgN)
def quickSort(arr,low,high): 
    if low < high:
        partIndex = partition(arr, low, high)
        #recursively sorts elements before/after partitionIndex
        quickSort(arr, low, partIndex - 1)
        quickSort(arr, partIndex + 1, high)
    #write your code here
  
# Driver code to test above
arr = [10, 7, 12, 14, 222, 8, 9, 1, 5, 5]
arr1 = [20, 19, 18, 16, 14, 3, 2] 
n = len(arr1) 
quickSort(arr1,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr1[i]), 
  
 
