# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# defining the binary serch
def binarySearch(arr, l, r, x): 
    while  l<=r:
        mid =l+(r-l)//2
# checking if the x is at mid then return mid
        if arr[mid] ==x:
            return mid
# if the x is greater than element at mid  then ignore the left half
        elif arr[mid]<=x:
            l=mid+1
# if the x is less than element at mid then ignore the right half
        else:
            r=mid-1
# if none of the element is  matching in an array then return -1
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
