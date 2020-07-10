# Python program for implementation of MergeSort 

def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0

    merged_list = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            i += 1

        else:
            merged_list.append(arr2[j])
            j+=1

    while i < len(arr1):
        merged_list.append(arr1[i])
        i+=1

    while j < len(arr2):
        merged_list.append(arr2[j])
        j+=1

    return merged_list


def mergeSort(arr):
    start = 0
    end = len(arr)
    #write your code here
    if start < end-1:
        mid = start + (end-start)//2
        left_sorted = mergeSort(arr[0:mid])
        right_sorted = mergeSort(arr[mid:end])
        return merge(left_sorted, right_sorted)

    else:
        return arr

# Code to print the list
def printList(arr): 
    
    #write your code here
    for element in arr:
        print(element)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sorted_arr = mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(sorted_arr)
