# Python program for implementation of MergeSort 

## Time Complexity = O(NlogN) as we recursively divide the array in half and merge them after sorting them
## Space Complexity  =  O(N) as we use auxillary arrays to store left and right sub arrays

def mergeSort(arr):
  if len(arr)==1:
    return
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  mergeSort(left)
  mergeSort(right)
  i,j,k=0,0,0
  while(i<len(left) and j<len(right)):
    if left[i]<right[j]:
      arr[k] = left[i]
      i+=1
      k+=1
    elif right[i] < left[j]:
      arr[k] = right[j]
      j+= 1
      k+=1
    else:
      arr[k] = right[j]
      arr[k] = left[i]
      i+=1
      k+=2
      j+=1
  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1
  while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in arr:
    print(i, end=" ")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
