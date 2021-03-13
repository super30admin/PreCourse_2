# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    mid = 0
  #write your code here
    while (l <= r):
        mid = (l+r)//2

#         print(mid ,"----", arr[mid] )
#         print(x)
            
        if (x < arr[mid]):
            r = mid -1
        elif (x > arr[mid]):
            l = mid + 1
        else:
            return mid
        
    return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 30
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
