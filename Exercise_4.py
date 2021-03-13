# Python program for implementation of MergeSort 
def mergeSort(arr):
    
  #write your code here
    # for dividing the array upto a point where only one element is left
    # then merge the elements based on order
    if len(arr) > 1:
        mid = len(arr)//2
        
        # call mergesort on left part
        left_part = arr[:mid]
        mergeSort(left_part)
        
        # call mergesort on right part
        right_part = arr[mid:]
        mergeSort(right_part)
        
        
        # this step takes place after all the partitions are done
        i = j = k = 0
        # Compare the 
        while(i < len(left_part) and j < len(right_part)):
            if (left_part[i] < right_part[j]):
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
                
            k += 1
        while(i < len(left_part)):
            arr[k] = left_part[i]
            i += 1
            k += 1
            
        while(j < len(right_part)):
            arr[k] = right_part[j]
            j += 1
            k += 1
            
            
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for k in range(len(arr)):
        print(arr[k], end = " ")
    
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
