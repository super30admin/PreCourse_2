class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    // TC: O(N), where N = r - l + 1 (Max = size of array).
    // SC: O(N), where N = r - l + 1 (Max = size of array).
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       /**
        * 
        Create a temp array of size r - l + 1
        Keep sorted elements from arr[l-r] inside tmp
        copy contents of tmp to arr within index l to r.
        */
       int[] tmp = new int[r - l + 1];
        int p1 = l;
        int p2 = m + 1;
        int k = 0;
        while(p1 <= m && p2 <= r)
        {
            if(arr[p1] <= arr[p2])
            {
                tmp[k++] = arr[p1++];
            }
            else 
            {
                tmp[k++] = arr[p2++];
            }
        }

        while(p1 <= m)
        {
            tmp[k++] = arr[p1++];
        }

        while(p2 <= r)
        {
            tmp[k++] = arr[p2++];
        }

        k = 0;
        for(int i = l; i <= r; i++)
        {
            arr[i] = tmp[k++];
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    // TC: O(N Lg N)..
    // SC: O(N).. From merge method
    void sort(int arr[], int l, int r) 
    { 
        if(l < r)
        {
            int mid = l + (r-l) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
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