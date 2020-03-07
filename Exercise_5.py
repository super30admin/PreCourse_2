# Python program for implementation of Quicksort

## Time Complexity = O(N^2) in worst case and O(NlogN) in average case
## Space Complexity  =  O(logN) average case  and O(N) worst case as we use additional space in stack

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l-1
  for j in range(l, h):
      if arr[j] < pivot:
          i += 1
          arr[j], arr[i] = arr[i], arr[j]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l,h)]
  while stack:
    l, h = stack.pop()
    if l>=h:
      continue
    piv = partition(arr, l, h)
    stack.append((l, piv-1))
    stack.append((piv+1,h))


a = [1, 4, 7, 2, 4, 5, 10, 13, 11, 32, 6, 9, 8, 0, -1]
quickSortIterative(a,0,len(a)-1)
print(a)


