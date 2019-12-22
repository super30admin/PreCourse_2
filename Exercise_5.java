class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//swapping without extra variable 
    	if (i != j) {        
    		/* not same object */
            if (arr[i] > 0 != arr[j] > 0) {
                /* not same sign */
            	swapWithoutExtraVariable(arr,i,j);
            } else {
            	//change the sign else it will result in 0 
                arr[i] = -arr[i];
                swapWithoutExtraVariable(arr,i,j);
                arr[j] = -arr[j];
            }
        }
    } 
    void swapWithoutExtraVariable(int arr[], int i, int j)
    {
    	arr[i] = arr[i] + arr[j];
    	arr[j]= arr[i] - arr[j];
    	arr[i]= arr[i]- arr[j];
    }
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot = arr[h];
    	int i=l-1;
    	for(int j=l ;j<h;j++)
    	{
    		if(arr[j]<pivot)
    		{
    			i++;
    			swap(arr,j,i);
    		}
    	}
    	swap(arr,h,i+1);
    	
    	return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	//initialize stack by size of the array which is high-low+1
    	int[] stack = new int[h-l+1];
    	int top=-1;
    	
    	//increment top and push low and high. high should be on top
    	stack[++top]=l;
    	stack[++top]=h;
    	
    	while(top>=0)
    	{
    		h=stack[top--];
    		l=stack[top--];
    		//get partition index
    		int p= partition(arr,l,h);
    		
    		if(p-1 >l)
    		{
    			stack[++top] = 	l;
    			stack[++top] = p-1;
    		}
    		
    		if (p+1 < h) { 
                stack[++top] = p+1; 
                stack[++top] = h; 
            } 
    	}
    	
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 