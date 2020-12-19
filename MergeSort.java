class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int len1 = m - l + 1;


       
       int len2 = r - m;

       int temp1[] = new int[len1];
       int temp2[] = new int[len2];

       for (int i=0; i< len1 ; i++)
            temp1[i] = arr[l+i];
       for (int j = 0 ; j < len2; j++)
            temp2[j] = arr[m+j+1];
    
       int k = l;
       int i=0, j=0;

       while ((i<len1) && (j<len2))
       {
           if(temp1[i] <= temp2[j])
           {
               arr[k] = temp1[i];
               i++;
           }
           else
           {
               arr[k] = temp2[j];
               j++;
           }
           k++;
        }
        while(i<len1)
        {
            arr[k] = temp1[i];
            i++;
            k++;
        }
        while(j<len2)
        {
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
            int m = (r+(l-1))/2;

            sort(arr, l, m);
            sort(arr, m+1, r);

            merge(arr, l, m, r);
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