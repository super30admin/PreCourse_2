# Python program for implementation of Quicksort Sort

# first selects the last element in the array as pivot and then places the element in the index position such that all the elements
# to the left of the picot is smaller than pivot and right to pivot is larger in their original sequence
#  Time Complexity = O(n) Space Complexity = O(1)

def partition(arr,low,high):
    i = low -1
    p = arr[high]
    # j traveres from first element to the last but one element
    for j in range(low,high):
        if arr[j] <= p:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return(i+1)

# Function to do Quick sort
# recursively calls itself and finds pivot for each divided array array
# Time Complexity= O(n)
# Space Complexity = O(1)
def quickSort(arr,low,high):
    if low>high:
        return
    else:
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print (arr[i])
