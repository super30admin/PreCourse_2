# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# first selects the last element in the array as pivot and then places the element in the index position such that all the elements
# to the left of the picot is smaller than pivot and right to pivot is larger in their original sequence
#  Time Complexity = O(n) Space Complexity = O(1)
def partition(arr, low, high):
    i = low -1
    p = arr[high]
    for j in range(low,high):
        if arr[j] <= p:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return(i+1)

# Instead of the recursive calls , a stack is created and the start and last elements of the array are pushed into the stack
# pop 2 elements from stack(start and last of the array) and send it to partition function to get the pivot. Continue dividing the array based
# on the pivot element
#Time Complexity = O(n)
# Space Complexity = O(n)
def quickSortIterative(arr, l, h):
    #create a stack
    stack = [0]*(h-l+1)
    i=0
    #pushing l , h values to stack
    stack[i] = l
    i = i+1
    stack[i] = h

    #keep popping until the stack is empty
    while i >= 0:

        h = stack[i]
        i =i-1
        l = stack[i]
        i = i-1
        p = partition(arr,l,h)
        if p-1 >l:
            i = i+1
            stack[i]= l
            i= i+1
            stack[i] = p-1
        if p+1 <h:
            i = i+1
            stack[i]= p+1
            i= i+1
            stack[i] = h

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print (arr[i])
