package PreCourses2;

/*
Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n ^ 2)

Space Complexity:
    O(1)
*/

public class IterativeQuickSort {

    private void sort(int[] arr, int low, int high) {
        if(low < high) {
            int p = partitionArray(arr, low, high);
            sort(arr, low, p - 1);
            sort(arr, p + 1, high);
        }
    }

    private int partitionArray(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for(int j = low ; j < high ; j++) {
            if(arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    private static void printArray(int[] arr) {
        for(int i = 0 ; i < arr.length ; i++) {
            System.out.print(arr[i] + " ");
        }
    }


    public static void main(String[] args) {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        System.err.println("Unsorted array:");
        printArray(arr);

        IterativeQuickSort ob = new IterativeQuickSort();
        ob.sort(arr, 0, n-1);

        System.err.println("\nSorted array:");
        printArray(arr);
    }
}