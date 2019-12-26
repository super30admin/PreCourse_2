# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        Left_subarray = mergeSort(arr[:mid])
        Right_subarray = mergeSort(arr[mid:])

        # print(Left_subarray,Right_subarray,mid)
        i = j = k = 0

        while i < len(Left_subarray) and j < len(Right_subarray):
            if Left_subarray[i] < Right_subarray[j]:
                arr[k] = Left_subarray[i]
                i += 1
                k += 1
            else:
                arr[k] = Right_subarray[j]
                j += 1
                k += 1
        while i < len(Left_subarray):
            arr[k] = Left_subarray[i]
            i += 1
            k += 1
        while j < len(Right_subarray):
            arr[k] = Right_subarray[j]
            j += 1
            k += 1
    return arr
# Code to print the list 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])



# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
