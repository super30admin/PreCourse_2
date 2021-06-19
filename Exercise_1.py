# Time Complexity : O(logN), Best Case: O(1), Worst Case: O(N), 
# Space Complexity : O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if r >= l:
    mid = (l + r) // 2
    if arr[mid] == x: # check if mid element is equal to key 
      return mid
    elif arr[mid] > x: # check if mid element is less ths key
      return binarySearch(arr, l, mid-1, x)
    else: # mid element is greater than key
      return binarySearch(arr, mid+1, r, x)
  else: # no element found
    return -1

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index ", result)
else: 
    print("Element is not present in array")
