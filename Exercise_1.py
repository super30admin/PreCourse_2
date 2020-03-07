# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

## Time Complexity = O(logN) as we discard half of the array every time in the while loop
## Space Complexity  =  O(1) as we dont use any additional space
def binarySearch(arr, l, r, x): 
  while(l<=r):
    mid = l+(r-l)//2
    if arr[mid]==x:
      return mid
    elif arr[mid] > x:
      r=mid-1
    else:
      l=mid+1
  return -1
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
