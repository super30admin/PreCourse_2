# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1

# Time complexity = O(logn) Space complexity=O(1)
# The recurrsive call divides the array into halves each time
def binarySearch(arr, l, r, x):
    if len(arr) == 0:
        return -1
    mid = int((l+r)/2)
    #print(mid)
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return binarySearch(arr,mid+1,r,x)
    else:
        return binarySearch(arr,l,mid-1,x)

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)


if result != -1:
    print ("Element is present at index {}".format(result))
else:
    print ("Element is not present in array")
