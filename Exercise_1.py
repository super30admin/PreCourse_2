# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
# Function for iterative binary search
def binarySearch(arr, l, r, x): 
  
    #write your code here
    while l<=r:
        mid = (r+l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            r = mid -1 
        else:
            l = mid +1
    return -1
  
# Time complexity: O(log n) where n=length of input array
# Space complexity: O(1)   
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
