#Time Complexity : O(n log n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : No

# Python program for implementation of Quicksort

def partition(arr, l, h):
  pIndex = l
  pivot = arr[h]
  for i in range(l, h):
    if arr[i] < pivot:
      arr[pIndex], arr[i] = arr[i], arr[pIndex]
      pIndex += 1
  arr[h], arr[pIndex] = arr[pIndex], arr[h]
  return pIndex



def quickSortIterative(arr, l, h):
  stack = [0] * (h-l+1)
  top = -1
  top += 1
  stack[top] = l
  top += 1
  stack[top] = h

  while top >= 0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    pIndex = partition(arr, l, h)

    if pIndex - 1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = pIndex - 1

    if pIndex + 1 < h:
      top += 1
      stack[top] = pIndex + 1
      top += 1
      stack[top] = h

if __name__ == "__main__":
  arr = [39, 119, 4,1,6,8,2, 100, 52]
  n = len(arr)
  quickSortIterative(arr,0,n-1)
  print(arr)


