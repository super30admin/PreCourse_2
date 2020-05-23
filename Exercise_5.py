# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1 
  
  for j in range(l,h):
    if arr[j] < pivot:
      i += 1 
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  if l < h:
    partition_index = partition(arr,l,h)
    quickSortIterative(arr,l, partition_index-1)
    quickSortIterative(arr,partition_index,h)

if __name__ == "__main__":
  arr = [5,4,3,2,1]
  quickSortIterative(arr, 0 , 4)
  print(arr)
