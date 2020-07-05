
def merge(arr, start, mid, end): 
	n1 = mid - start + 1
	n2 = end- mid 

	# create temp arrays 
	L = [0] * (n1) 
	R = [0] * (n2) 

	# Copy data to temp arrays L[] and R[] 
	for i in range(0 , n1): 
		L[i] = arr[start + i] 

	for j in range(0 , n2): 
		R[j] = arr[mid + 1 + j] 


	i = 0	 # Initial index of first subarray 
	j = 0	 # Initial index of second subarray 
	k = start	 # Initial index of final merged subarray 

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			arr[k] = L[i] 
			i += 1
		else: 
			arr[k] = R[j] 
			j += 1
		k += 1


	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1


	while j < n2: 
		arr[k] = R[j] 
		j += 1
		k += 1


def mergeSort(arr,start,end): 
	if start < end: 


		mid = (start+(end-1))//2

	
		mergeSort(arr, start, mid) 
		mergeSort(arr, mid+1, end) 
		merge(arr, start, mid, end) 
def printList(arr): 
    

    for i in range(len(arr)): 
        print ("%d" %arr[i]), 


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
