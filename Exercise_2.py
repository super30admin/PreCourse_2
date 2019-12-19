# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
	#Taking last element to be pivot
	pivot = arr[high]
	i = low-1#initialize i pointer
	for j in range(low,high):
		if arr[j] < pivot:
			i += 1
			#Swap the lements
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return (i+1)
		
# Function to do Quick sort 
def quickSort(arr,low,high):
	if low < high:
		#Place pivot at right place
		piv = partition(arr,low,high)
		quickSort(arr,low,piv-1)
		quickSort(arr,piv+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
