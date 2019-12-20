# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # We use divide and conquer strategy for finding the element in the sorted array
  # We first take the key, compare it with the middle element of the array and see whether they are equal
  # If they are equal, we then return the middle. Otherwise, if the key is greater than the middle, we then recursively search in the right half
  # Else, we recursively search in the left half
  # We continue like this until the size of the array becomes one, i.e, when l = r. 
  # If we cant find the element even after performing these steps, and when l > r, we return -1
  # Time complexity is O(logn) 
  if l <= r:
    mid = int((l+r)/2)
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      return binarySearch(arr, mid + 1, r, x)
    else:
      return binarySearch(arr, l, mid, x)
  else:
    return -1        
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
