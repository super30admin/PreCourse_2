# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
    
    if len(arr)>1:
        subArr_left = arr[:len(arr)//2]
        subArr_right = arr[len(arr)//2:]
        
        mergeSort(subArr_left)
        mergeSort(subArr_right)
        
        #merging
        i = 0 # index for subArr_left
        j = 0 # index for subArr_right
        k = 0 # index for merged array 
        
        while i < len(subArr_left) and j < len(subArr_right):
            if subArr_left[i]<subArr_right[j]:
                arr[k] = subArr_left[i]
                i += 1
                k += 1
            else:
                arr[k] = subArr_right[j]
                j += 1
                k += 1
                
        # after all comparisons, if there are still elements left in the left array,
        while i < len(subArr_left):
            arr[k] = subArr_left[i]
            i += 1
            k += 1
            
        # similarly, if there are elements left in the right array,
        while j < len(subArr_right):
            arr[k] = subArr_right[j]
            j += 1
            k += 1

            # log n merging for n items, hence O(n log n) complexity    
  
# Code to print the list
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)): 
        print ("%d" %arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

