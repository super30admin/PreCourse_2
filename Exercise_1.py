# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    if l <=r:
        mid =  (r + l)-1//2

        if x == arr[mid]:
            return mid
        if x > arr[mid]:
            return binarySearch(arr, mid+1, r, x)
        else:
            return binarySearch(arr, l, mid-1, x)

    else:
        return -1
    
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 0
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
