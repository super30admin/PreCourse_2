Time Complexity-Worst-O(n^2)-always the highest is pivot
                Average-O(nlogn)
Space Complexity-O(1)
 

public class QuickSort {

    void swap(int arr[], int i, int j) {
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    int partition(int arr[], int low, int high) {

        int pivot=high;
        int s=low;
        for(int i=low;i<pivot;i++)
        {
            if(arr[i]<arr[pivot])
            {
                swap(arr,s,i);
                s++;
            }

        }
        swap(arr,s,pivot);
        return s;
    }

    void sort(int arr[], int low, int high) {

        if(low<high)
        {
            int p=partition(arr,low,high);
            sort(arr,low,p-1);
            sort(arr,p+1,high);
        }
    }


    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);

    }
}



