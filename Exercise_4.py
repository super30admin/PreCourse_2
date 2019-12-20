# Python program for implementation of MergeSort 
def mergeSort(arr, left, right):
  if left < right:
    middle = (left + right) // 2
    mergeSort(arr, left, middle)
    mergeSort(arr, middle + 1, right)
    merge(arr, left, middle, right)
  #write your code here

def merge(arr, left, middle, right):
  # Partition the array in the middle, and store the left half in larr
  # And right half in rarr
  larr = arr[left : middle + 1]
  rarr = arr[middle + 1: right + 1]

  i = j = 0
  index = left # left index of main array

  # Have i pointer starting from 0 for the larr and 
  # j pointer starting from 0 for the rarr
  # If element at located at i index of left array is lesser than 
  # element located at j index of right array, copy the lesser element
  # on to the main array at its index.
  while i < len(larr) and j < len(rarr):
    if larr[i] < rarr[j]:
      arr[index] = larr[i]
      i+=1
    else:
      arr[index] = rarr[j]
      j+=1
    index += 1

  # Copy over the remaining larr and rarr elements onto the main array
  while i < len(larr):
    arr[index] = larr[i]
    i+=1
    index += 1

  while j < len(rarr):
    arr[index] = rarr[j]
    j+=1
    index+= 1        



def printList(arr):
  print(str(arr))
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [2, 12, 11, 13, 5, 6, 7, 0, 1,4,3,7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0, len(arr) - 1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
