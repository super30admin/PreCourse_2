package PreCourses2;

/*
Time Complexity :
    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(log n)

Space Complexity :
    O(1)
*/

public class binarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] == x)  return mid;

            if(arr[mid] > x) return binarySearch(arr, l, mid - 1, x);

            if(arr[mid] < x) return binarySearch(arr, mid + 1, r, x);
        }
        return -1;
    }

    public static void main(String[] args) {
        binarySearch ob = new binarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.err.println("Element not present");
        else
            System.err.println("Element found at index " + result);
    }
}
