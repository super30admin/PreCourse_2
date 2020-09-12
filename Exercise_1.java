//Time Complexity - O(logn) - where n is the number of elements to array.
//Spcae Complexity - O(1) - Constant Space.


class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r>=l){
            int pivot = l+(r-l)/2;
            if(arr[pivot]==x) return pivot;
            if(arr[pivot]>x) return binarySearch(arr, l, pivot-1, x);
            if(arr[pivot]<x) return binarySearch(arr, pivot+1, r, x);
        }
        return -1;
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
