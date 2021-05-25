class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	int i = low;
    	int j = high + 1;
    	while(true) {
	    	//find index on the left to swap
	    	while(arr[++i] < arr[low])
	    		if(i == high)
	    			break;
	    	//find index on the right to swap
	    	while(arr[low] < arr[--j])
	    		if(j == low)
	    			break;
	    	//check if pointers cross
	    	if(i >= j)
	    		break;
	    	swap(arr,i,j);
    	}
    	//swap with partition item
    	swap(arr,low,j);
    	//return index of inplace item
    	return j;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
    	if(high <= low)
    		return;
    	int pivotIndex = partition(arr, low, high);
    	sort(arr,low,pivotIndex-1);
    	sort(arr,pivotIndex+1,high);
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
    /*Time Complexity : 0(n log n)
     * Space Complexity: O(n)*/
} 
