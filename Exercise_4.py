# Python program for implementation of MergeSort 
def mergeSort(arr):
  mid = len(arr) // 2
  l = arr[:mid]
  r = arr[mid:]

  i = j = k = 0
  while i < len(l) and j < len(r):
    if l[i] < r[i]:
      arr[k] = l[i]
      i += 1
    else:
      arr[k] = r[j]
      j += 1
    k += 1
  
  while i < len(l):
    arr[k] = l[i]
    k += 1
    i += 1

  while j < len(r):
    arr[k] = r[j]
    k += 1
    j += 1
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
