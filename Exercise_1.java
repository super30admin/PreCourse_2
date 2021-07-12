class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    // TC: O(Lg N). Where N = r - l + 1 (Or size of array)
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int result = -1;
        while(l <= r)
        {
            int mid = l + (r - l) / 2;
            if(x == arr[mid])
            {
                result = mid;
                break;
            }
            else if(x > arr[mid])
            {
                l = mid + 1;
            }
            else 
            {
                r = mid - 1;
            }
        }

        return result;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
