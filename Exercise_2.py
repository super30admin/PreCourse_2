# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    count =0
    p= low
    q= high

    for i in range(low, high+1):
        if arr[i]<arr[p]:
            count+=1
    
    #swap first element to place it at right position
    arr[low], arr[low+count]= arr[low+count], arr[low]

    for i in range(0, count):
        if arr[p]< arr[low+count]:
            p+=1
        elif arr[q]>arr[low+count]:
            q-=1
        else:
            arr[p], arr[q] = arr[q], arr[p]
            p+=1
            q-=1
    return low+count

  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low>=high:
        return
    
    pivot= partition(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
