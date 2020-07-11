# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    if l > r:
        return -1
    
    mid = l + (r - l) / 2
    
    if arr[mid] == x:
        return mid
    
    if arr[mid] > x:
        # search left
        return binarySearch(arr, l, mid - 1, x)
    
    if arr[mid] < x:
        # search right
        return binarySearch(arr, mid + 1, r, x)


# write your code here


# Test array 
arr = []
x = 1

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print "Element is present at index % d" % result
else:
    print "Element is not present in array"
