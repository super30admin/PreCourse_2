# Python program for implementation of Quicksort
#swap index values
def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
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

#to replace recursion to iterative.. push parameters you would pass into a stack
# Function to do Quick sort..time:O(nlgn) at best O(N^2) at worse space:O(lgN)
def quickSortIterative(arr, l, h):
  #write your code here
  if not arr:
    return arr 
  
  stack = []
  stack.append(l)
  stack.append(h)

  while stack: 
    #when popping... high then low because high is what is put in last
    high = stack.pop()
    low = stack.pop() 

    partIndex = partition(arr, low, high)
    #recursive conversion to iteration: quickSort(arr, low, partIndex - 1)
    if partIndex-1 > low:
      stack.append(low)
      stack.append(partIndex - 1)
    #recursive conversion to iteration: quickSort(arr, partIndex + 1, high)
    if partIndex + 1 < high:
      stack.append(partIndex+1)
      stack.append(high)


arr = [10, 7, 12, 14, 222, 8, 9, 1, 5, 5, 312398]
arr1 = [20, 19, 18, 16, 14, 3, 2, 123] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 