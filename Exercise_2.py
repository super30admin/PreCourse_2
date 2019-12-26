# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # write your code here
    i = low-1
    pivot = arr[high]
    # print(pivot)
    for j in range(low,high):

        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]

    return (i+1)

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    # write your code here
    if low < high:
        # print(arr)
        pi_high = partition(arr,low,high)

        quickSort(arr,low,pi_high-1)
        quickSort(arr,pi_high+1,high)


# Driver code to test above 
arr = [40,50,90,10,20,80,60]
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:")
for i in range(n): 
    print(arr[i])
