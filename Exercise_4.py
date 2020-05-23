# Python program for implementation of MergeSort 

# Time: O(nlog n) | space = O(nlog n), where n is the number of elements in an array
def mergeSort(arr):
  #write your code here
    if len(arr) > 1:
      middle = len(arr) // 2
      left = arr[:middle]
      right = arr[middle:]
      mergeSort(left)
      mergeSort(right)
      arr.clear()
      
      while len(left) > 0 and len(right) > 0 :
        if left[0] <= right[0]:
          arr.append(left[0])
          left.pop(0)
        else:
          arr.append(right[0])
          right.pop(0)
      
      for c in left:
        arr.append(c)
        
      for c in right:
        arr.append(c)
        
# Code to print the list 
def printList(arr): 
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
