# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    #write your code here
    pivot_element = arr[high]
    slow_ptr = low
    fast_ptr = low

    while fast_ptr < high:
        if arr[fast_ptr] < pivot_element:
            arr[slow_ptr], arr[fast_ptr] = arr[fast_ptr], arr[slow_ptr]
            slow_ptr +=1
        fast_ptr +=1

    arr[slow_ptr], arr[high] = arr[high], arr[slow_ptr]

    return slow_ptr


def quickSortIterative(arr, l, h):
    #write your code here
    stack = []
    stack.append(l)
    stack.append(h)

    while stack:
        h = stack.pop()
        l = stack.pop()
        pivot = partition(arr, l, h)

        if pivot > l+1:
            stack.append(l)
            stack.append(pivot-1)

        if pivot < h-1:
            stack.append(pivot+1)
            stack.append(h)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

