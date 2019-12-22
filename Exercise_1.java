class BinarySearch { 
	
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearchIterative(int arr[], int l, int r, int x)
    {
    	//do until left index is smaller than right index else element is not present, out of loop
    	while(l<=r)
    	{
    		//check for middle index
    		int mid=(l+r)/2;
    		//if found return it
    		if(x==arr[mid])
    			return mid;
    		//else check for right half if element is bigger than mid 
    		else if(x > arr[mid])
    			l=mid+1;
    		//else check for left half if element is smaller than mid
    		else
    			r=mid-1;
    	}
    	//once l>r means element not found, return -1
    	return -1;
    }
    
    //recursive approach
    int binarySearchRecursive(int arr[], int l, int r, int x)
    {
    	//find mid
    	int mid=(l+r)/2;
    	
    	//do until left index is lesser than right index
    	while(l<=r)
    	{
    	// start from mid as we are doing binary means divide array by half.if mid matches , return mid
    	if(x==arr[mid])
			return mid;
    	else if(x > arr[mid])
    		//call function again for right half
    		return binarySearchRecursive(arr,mid+1,r,x);
		//else check for left half if element is smaller than mid
		else
			//call function for left half
			return binarySearchRecursive(arr,l,mid-1,x);
    	}
    	//if nothing is found
			return -1;
    	
    }
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 3; 
        int result = ob.binarySearchRecursive(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
