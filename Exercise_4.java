// Time Complexity :O(nlogn)
// Space Complexity :0(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int size1 = m - l + 1;
       int size2 = r -m;

       int[] temp1 = new int[size1];
       int[] temp2 = new int[size2];

       for(int i=0;i<size1;++i) temp1[i] = arr[l+i];
       for(int i=0;i<size2;++i) temp2[i] = arr[m+i+1];

       int i = 0, j = 0; 
       int k = l; 
        while (i < size1 && j < size2) { 
            if (temp1[i] <= temp2[j]) { 
                arr[k] = temp1[i]; 
                i++; 
            } 
            else { 
                arr[k] = temp2[j]; 
                j++; 
            } 
            k++; 
        }
        while (i < size1) { 
            arr[k] = temp1[i]; 
            i++; 
            k++; 
        } 
        while (j < size2) { 
            arr[k] = temp2[j]; 
            j++; 
            k++; 
        }  

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r)
        {
            int middle = (l+r)/2;
            sort(arr, l, middle);
            sort(arr, middle+1, r);
            merge(arr, l, middle, r);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 