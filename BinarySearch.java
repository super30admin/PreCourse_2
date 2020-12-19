import javax.lang.model.util.ElementScanner14;

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int median = 0;
        if(r>=l){
            if (l < r)
                median = l + ((r-1)/ 2) ;
            else
                median = l;
        
        if(arr[median] == x)
            return median;
        else if(arr[median] > x)
            binarySearch(arr, l, median-1, x);

        return binarySearch(arr, median+1, r, x);
        } 
        return -1;
    }
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 40; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
