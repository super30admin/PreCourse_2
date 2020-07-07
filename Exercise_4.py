# Python program for implementation of MergeSort 
from collections import deque

#Function to preform mergesort
def mergeSort(arr):
    if len(arr)>1: 
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        arr = deque([])
        while left and right:
            if left[0] < right[0]:
                arr.append(left[0])
                left.popleft()
            else:
                arr.append(right[0])
                right.popleft()
           
        for l in left:
            arr.append(l)

        for r in right:
            arr.append(r)
    return deque(arr)

  
# Code to print the list 
def printList(arr): 
    for a in arr:
        print(a, end=" ")
    print("\n")
    #write your code here

# Time complexity: O(nlogn)
# Space complexity: O(n) where n is the length of input array
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 0, 9, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr =mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
