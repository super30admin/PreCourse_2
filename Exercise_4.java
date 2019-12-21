class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int SubLength1 = m - l + 1;
       int SubLength2 = r - m;

       int[] TempLeft = new int[SubLength1];
       int[] TempRight = new int[SubLength2];

        for (int i = 0; i < SubLength1; ++i){
            TempLeft[i] = arr[l + i];
        }
        for (int j = 0; j < SubLength2; ++j){
            TempRight[j] = arr[m + 1+ j];
        }

        int i = 0;
        int j = 0;

        int k = l;
        while (i < SubLength1 && j < SubLength2)
        {
            if (TempLeft[i] <= TempRight[j])
            {
                arr[k] = TempLeft[i];
                i++;
            }
            else
            {
                arr[k] = TempRight[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < SubLength1)
        {
            arr[k] = TempLeft[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < SubLength2)
        {
            arr[k] = TempRight[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
      if(l < r) {
          int mid = (l+r)/2;

          sort(arr, l, mid);
          sort(arr, mid+1, r);
          merge(arr, l, mid, r);
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