// Time Complexity :O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
         if(r<l)
        {
            return 0;
        }
        int mid=l+(r-l)/2;
        while(l<r)
        {
            if(arr[mid]==x)
            {
                return mid;
            }
             if (arr[mid]>x)
            {
               return binarySearch( arr,l,mid-1,x);
            }
             if(arr[mid]<x)
            {
            	return binarySearch( arr,mid+1,r,x);
              
            }
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
