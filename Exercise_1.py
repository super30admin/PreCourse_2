  
#Time Complexity : O(log n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  while l < r:
    mid = (l + r) //2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      l += 1
    else:
      r -= 1
  return -1
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 0
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
