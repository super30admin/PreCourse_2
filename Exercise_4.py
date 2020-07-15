#Time Complexity : O(n log n)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : No

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) < 2:
    return
  def merge(arr, left, right):
    i, j, k = 0,0,0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1
      
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  
  l = []
  r = []
  for x in range(len(arr)//2):
    l.append(arr[x])
  for y in range(len(arr)//2, len(arr)):
    r.append(arr[y])
  mergeSort(l)
  mergeSort(r)
  merge(arr, l, r)


  

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
   print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
