# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  
  #write your code here

    while l<r:
        mid_point = (l+4)//2

        if (x == arr[mid_point]):
            return mid_point
        elif (x < arr[mid_point]):
            r = mid_point - 1
        else:
            l = mid_point + 1

    return -1

    # Complexity O(log n)
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
