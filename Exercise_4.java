class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int left [] = new int[m -l +1];
        int right [] = new int[r - m];

        for(int i=0; i< left.length; i++)
            left[i] = arr[l + i];

        for(int i=0; i< right.length; i++)
            right[i] = arr[m+1 + i];

        int i=0, j=0; // left - i right - j
        int k=l; // arr final sorted
        while( i< left.length && j< right.length)
        {
            if(left[i]< right[j])
            {
                arr[k] = left[i];
                i++;
            }
            else
            {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while( i < left.length)
            arr[k++] = left[i++];

        while( j <right.length)
            arr[k++] = right[j++];

    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l>=r)
        {
            return;
        }
        int mid = l + (r-1) / 2;
        sort(arr, l, mid-1);
        sort(arr, mid+1,r);

        merge(arr, l, mid, r);
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
