# Python code to implement iterative Binary  
# Search.   
# It returns location of x in given array arr  
# if present, else returns -1 

# Time: O(log n) | Space: O(1), where log is base 2, and n is the number of elements in an array. 
def binarySearch(arr, l, r, target): 
  #write your code here
  while l <= r : 
    middle = (l+r)//2
    if arr[middle] == target:
      return middle
    elif arr[middle] < target:
      l = middle + 1
    else:
      r = middle 
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
