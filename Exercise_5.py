# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# same as recursive
def partition(arr, l, h):
  #write your code here

    mid = (h+l)//2
    pivot = h
    
    if arr[l] < arr[mid]:
        if arr[mid] < arr[h]:
            pivot = mid
    
    elif arr[l] < arr[h]:
        pivot = l
        
    pivotVal = arr[pivot]
    
    arr[pivot], arr[l] = arr[l], arr[pivot] 
    x = l # first pointer
    
    for i in range(l, h+1):
        if arr[i] < pivotVal:
            x += 1
            arr[i], arr[x] = arr[x], arr[i] 
            
    arr[l], arr[x] = arr[x], arr[l] 
    
    return x

class Stack:    
    def __init__(self):
        self.items = []    
        
    def push(self, element):
        self.items.append(element)   
        
    def pop(self):
        return self.items.pop()    
    
    def is_empty(self):
        return self.items == []

def quickSortIterative(arr, l, h):
  #write your code here

    stack = Stack()
    stack.push(l)
    stack.push(h)
  
    while stack.is_empty() is False:
        h = stack.pop()
        l = stack.pop()
        part = partition(arr,l,h)
  
        if part - 1 > l:
            stack.push(l)
            stack.push(part - 1)

        if part + 1 < h:
            stack.push(part +1)
            stack.push(h)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])