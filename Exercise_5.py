# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    i = l - 1
    pivot = arr[h]
    
    for j in range(l, h):
        if (pivot >= arr[j]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1



def quickSortIterative(arr, l, h):
  #write your code here
    
    stack = [0] * h
    top = -1
    
    
    top += 1
    stack[top] = l
    
    top += 1
    stack[top] = h
    
    while(top >= 0):
        h = stack[top]
        top -= 1
        
        l = stack[top]
        top -= 1
        
        ipart = partition(arr, l, h)
        
        if ipart-1 > l:
            top += 1
            stack[top] = l
            
            top += 1
            stack[top] = ipart -1
        
        if ipart+1 < h:
            top += 1
            stack[top] = ipart + 1
            
            top += 1
            stack[top] = h

            
arr = [10, 80, 20, 40]
quickSortIterative(arr, 0, len(arr)-1)
print("Sorted array: ", arr)
