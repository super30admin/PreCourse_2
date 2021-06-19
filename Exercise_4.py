# Time Complexity : O(NlogN)
# Space Complexity : O(N)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
      mid = len(arr) // 2  # Find mid Element
      left = arr[:mid]
      right = arr[mid:]

      mergeSort(left)  #Sort the left side
      mergeSort(right) # Sort the right Side

      i = j = k = 0

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
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i], end= " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is: ")  
    printList(arr) 
    mergeSort(arr) 
    print()
    print("Sorted array is: ") 
    printList(arr) 
