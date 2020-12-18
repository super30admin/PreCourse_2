# Python program for implementation of MergeSort 
#Time complexity: O(nlgn) and Space: O(n)
def mergeSort(arr):
  if len(arr) == 1 or not arr:
    return arr
  #make sure arr length is greater than 1
  if len(arr) > 1:
    mid = len(arr) // 2

    #get left half and right half then do mergeSort on them
    leftSide = arr[:mid]
    rightSide = arr[mid:]
    mergeSort(leftSide)
    mergeSort(rightSide)

    i = j = k = 0
    #merge the two halves (left and right arrays)
    while i < len(leftSide) and j < len(rightSide):
      if leftSide[i] < rightSide[j]:
        arr[k] = leftSide[i]
        i += 1
      else:
        arr[k] = rightSide[j]
        j += 1 
      k += 1
    #one of the halves[] are empty at this point then just put the rest of the values in arr
    for index in range(i, len(leftSide)):
      arr[k] = leftSide[index]
      k += 1
    for index in range(j, len(rightSide)):
        arr[k] = rightSide[index]
        k += 1

  #write your code here
  
# Code to print the list 
#time: O(N), space:O(N) where N is array size
def printList(arr): 
    for i in arr:
      print(i, end=" ")
    print("\n")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
