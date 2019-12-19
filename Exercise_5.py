# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
	i = l - 1
	#Choosing pivot to be last element
	pivot = arr[h]
	for j in range(l,h):
		if arr[j] < pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[h] = arr[h],arr[i+1]
	return (i+1)
	
def quickSortIterative(arr, l, h):
	size = len(arr)
	stack = [0]*size
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
		piv = partition(arr,l,h)
		if piv - 1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = piv - 1
		if piv + 1 < h:
			top = top + 1
			stack[top] = piv + 1
			top = top + 1
			stack[top] = h
 
# Driver code to test above
arr = [10, 33, 7, 1, 13]
quickSortIterative(arr, 0, len(arr)-1)
print("Sorted array is:")
for i in range(len(arr)):
    print (arr[i], end= " ")