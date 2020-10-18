# Python program for implementation of Quicksort Sort 
  
# defining the partitioner function
def partitioner(arr,low,high):
    #considering the pivot element as last
    pivot=arr[high]
    i=low-1 # initializing the index of smaller element 
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            #swapping the elements 
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    
    return (i+1)

def quickSort(arr,low,high):
    if low<high:
        # pivot element  to be in right place
        p=partitioner(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=" ") 
  
 
