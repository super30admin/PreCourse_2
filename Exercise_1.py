# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  while l <= r:
    mid = (l+r)//2
    if arr[mid]==x:
      return mid
    elif arr[mid]>x:
      r = mid-1
    else:
      l = mid+1
  if l>r:
    return -1
    
 
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")

"""
the complexity of the binary search tree is O(logn) 
as we divide the array into two halves and search 
for the element in a single half.
""" 
