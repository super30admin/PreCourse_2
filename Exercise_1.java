class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) // time and space  O log(n) 
                                                     // reduce space to O(1) using iterative approach
    { 
        //Write your code here
        // finding the mid
        if (r >= l){
            int mid = l + (r-l) /2;
           
            if (arr[mid] == x)
               return mid; // returning index else
            
            if (arr[mid] > x) 
               return binarySearch(arr, l, mid - 1, x); 
            else
               return binarySearch(arr, mid + 1, r, x);      

        }
        return -1 ; // element not found.
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
