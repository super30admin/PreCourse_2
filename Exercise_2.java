class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    // TC: O(1)
    void swap(int arr[],int i,int j){
        //Your code here   
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    
    // TC: O(N)
   int partition(int arr[], int low, int high) 
    { 
        int piv = low;
        
        int s = low + 1, e = high;

        while(s <= e)
        {
            if(arr[s] <= arr[piv])
            {
                s++;
            }
            else if(arr[e] >= arr[piv])
            {
                e--;
            }
            else 
            {
                swap(arr, s, e);
                s++;
                e--;
            }
        }
        
        swap(arr, s - 1, piv);

        return s - 1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    // TC: O(N Lg N). (N ^ 2) In worst case
    // SC: O(Lg N).. Recursive Stack
   void sort(int arr[], int low, int high) 
    {  
            if(low < high)
            {
                int piv = partition(arr, low, high);
                sort(arr, low, piv - 1);
                sort(arr, piv + 1, high);
            }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
