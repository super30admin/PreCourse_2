# Python program for implementation of MergeSort 
def mergeSort(arr):
	#Edge case
	if len(arr) == 0:
		return []
	if len(arr) == 1:
		return arr
	mid = len(arr)//2
	#Divide the array into two
	left = arr[:mid]
	right = arr[mid:]
	mergeSort(left)
	mergeSort(right)
	
	#Joining the separated elements into single array and sorting by comparing them
	i = 0
	j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i]<right[j]:
			arr[k] = left[i]
			i += 1
			k += 1
		else:
			arr[k] = right[j]
			j += 1
			k += 1
	while i < len(left):#if j has reached end of right but i still has not reached end of lrft
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):#if i has reached end of left but j still has not reached end of right
		arr[k] = right[j]
		j += 1
		k += 1
# Code to print the list 
def printList(arr):
	for k in range(len(arr)):
		print(arr[k])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
