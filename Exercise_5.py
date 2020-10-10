# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    partition_index=0
    for i in range(l,h):
        if arr[i]<=arr[h]:
            arr[i],arr[partition_index]=arr[partition_index],arr[i]
            partition_index+=1
    arr[h],arr[partition_index]=arr[partition_index],arr[h]
    return partition_index
  #write your code here


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
            #write your code here
arr=[2,1,5,3,9,6]
quickSortIterative(arr,0,len(arr)-1)
print(arr)