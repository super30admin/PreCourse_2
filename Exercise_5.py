# This function is same in both iterative and recursive 
def partition(arr, l, h): 
    #write your code here
	i = ( l - 1 ) 
	x = arr[h] 

	for j in range(l, h): 
		if arr[j] <= x: 

			i = i + 1
			arr[i], arr[j] = arr[j], arr[i] 

	arr[i + 1], arr[h] = arr[h], arr[i + 1] 
	return (i + 1) 


def quickSortIterative(arr, l, h): 
    #write your code here

	size = h - l + 1
	stack = [0] * (size) 


	top = -1

	# push initial values of l and h to stack 
	top = top + 1
	stack[top] = l 
	top = top + 1
	stack[top] = h 

	# Keep popping from stack while is not empty 
	while top >= 0: 

		# Pop h and l 
		h = stack[top] 
		top = top - 1
		l = stack[top] 
		top = top - 1

		# Set pivot element at its correct position in 
		# sorted array 
		p = partition( arr, l, h ) 

		# If there are elements on left side of pivot, 
		# then push left side to stack 
		if p-1 > l: 
			top = top + 1
			stack[top] = l 
			top = top + 1
			stack[top] = p - 1

		# If there are elements on right side of pivot, 
		# then push right side to stack 
		if p + 1 < h: 
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h 

# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("% d" % arr[i]), 

