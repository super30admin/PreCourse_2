# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
   #  take the last element as pivot and
    #  place the elements less than pivot on left side and
    #  all elements greater than pivot on right side of it in the array
    pivot = arr[h]
    #lets say index of smallest element be low-1
    k = l -1
    for j in range(l, h):
        if arr[j]<pivot:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]
        # print(arr)
    arr[k+1], arr[h] = arr[h], arr[k+1]
    return (k+1)



def quickSortIterative(arr, l, h):
  size = h-l+1
  arr1 = [0]*(size)
  top = -1

  top = top+1
  arr1[top]=l
  top = top+1
  arr1[top]=h
  print(arr1)
  
  while top>=0:
    h = arr1[top]
    top = top-1
    l = arr1[top]
    top = top-1
    print(arr1)

    p = partition(arr, l, h)

    if p-1 >l:
      top = top+1
      arr1[top]=l
      top = top+1
      arr1[top]=p-1
      print(arr1)

    if p+1 < h:
      top = top+1
      arr1[top]=p+1
      top = top+1
      arr1[top]=h
      print(arr1)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

    

"""
Quick sort has O(nlogn) complexity in the best case where median element is selected as pivot.
it has O(n^2) complexity when smallest or largest element is picked as pivot.
"""


