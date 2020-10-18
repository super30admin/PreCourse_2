# Python program for implementation of MergeSort
#The function divides the array in the middle and calls itself recursively for each half separately
#when it reaches one element in each on the left and right halves, it starts merging by comparing the 2 divided subarrays and
#storing it in the original array
#Time Complexity = O(logn) Space Complexity= O(n)
def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)/2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k = 0

#Compares the elements in left and right array and copies to the original array
        while( i<len(left) and j <len(right)):
            if(left[i]<right[j]):
                arr[k] = left[i]
                i = i+1
            else:
                arr[k] = right[j]
                j = j+1
            k = k+1

#checks if there is any data left in the left and right arrays then it copies it to the original array
        while i< len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1
        while j< len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1

# Code to print the list
def printList(arr):
    for a in arr:
        print(a)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)
