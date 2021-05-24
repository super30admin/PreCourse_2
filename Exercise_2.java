// Time Complexity: O(n^2)
// Space Complexity: O(n logn) -> for each partition recursion we are forming a tree hence log n. And We are doing 'n' partitions .
//  Hence total space complexity is O(n logn)
class QuickSort {
    /*
     * This function takes last element as pivot, places the pivot element at its
     * correct position in sorted array, and places all smaller (smaller than pivot)
     * to left of pivot and all greater elements to right of pivot
     */
    void swap(int arr[], int i, int j) {
        // Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        int pivot = arr[high];
        int l = low, r = high;

        while (l < r) {
            while (arr[l] < pivot && l < r)
                l++;
            while (arr[r] >= pivot && l < r)
                r--;

            if (l < r)
                swap(arr, l, r);

        }
        swap(arr, l, high);
        return l;
    }

    /*
     * The main function that implements QuickSort() arr[] --> Array to be sorted,
     * low --> Starting index, high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        // Recursively sort elements before
        // partition and after partition

        if (low < high) {
            int index = partition(arr, low, high);
            sort(arr, low, index - 1);
            sort(arr, index + 1, high);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
