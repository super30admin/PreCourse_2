import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if(i == j) return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        int pivot = arr[high];
        int i = low - 1, j = low;
        // loop invariant
        // arr[low...i-1] contains elemets <= pivot
        // arr[i...j] contains elements > pivot
        // element at index j is the one being processed
        while (j < high) {
            if (arr[j] <= pivot) {
                swap(arr, i + 1, j);
                i++;
            }
            j++;
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.add(h);
        stack.add(l);
        while (stack.size() >= 2) {
            int low = stack.pop();
            int high = stack.pop();
            int p = partition(arr, low, high);
            if (p - 1 - low + 1 > 0) {
                stack.add(p - 1);
                stack.add(low);
            }
            if (high - (p + 1) + 1 > 0) {
                stack.add(high);
                stack.add(p+1);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}