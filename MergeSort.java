package PreCourses2;

/*
Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n log n)

Space Complexity:
    O(n) // creation of new array (lowArray + highArray)
*/

public class MergeSort {

    private void sort(int arr[], int arrLength) {
        if(arrLength < 2) return;
        int mid = arrLength / 2;
        int lowArray[] = new int[mid];
        int highArray[] = new int[arrLength - mid];

        for(int i = 0 ; i < mid ; i++) {
            lowArray[i] = arr[i];
        }
        for(int j = mid ; j < arrLength ; j++) {
            highArray[j - mid] = arr[j];
        }
        sort(lowArray, mid);
        sort(highArray, arrLength - mid);
        merge(arr, lowArray, highArray, mid, arrLength - mid);
    }

    private void merge(int arr[], int lowArray[], int highArray[], int lowLength, int highLength) {
        int i = 0;;
        int j = 0;
        int k = 0;


        while(i < lowLength && j < highLength) {
            if (lowArray[i] <= highArray[j]) {
                arr[k] = lowArray[i];
                i++;
            } else {
                arr[k] = highArray[j];
                j++;
            }
            k++;
        }

        while(i < lowLength) {
            arr[k] = lowArray[i];
            i++;
            k++;
        }

        while(j < highLength) {
            arr[k] = highArray[j];
            j++;
            k++;
        }
    }


    private static void printArray(int arr[]) {
        for(int i = 0 ; i < arr.length ; i++) {
            System.err.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array:");
        printArray(arr);

        MergeSort ob = new MergeSort();
//        ob.sort(arr, 0, arr.length-1);
        ob.sort(arr, arr.length);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}