Time Complexity-O(nlogn)
Space Complexity-O(1)

class MergeSort
{
    void merge(int arr[], int l, int m, int r)
    {
        int temp[] = new int[r - l + 1];
        int i = l, j = m+1, k = 0;

        while(i <= m && j <= r) {
            if(arr[i] <= arr[j]) {
                temp[k] = arr[i];
                i ++;
            }
            else {
                temp[k] = arr[j];
                j ++;
            }
            k++;
        }

        // add elements left in the first interval
        while(i <= m) {
            temp[k] = arr[i];
            k++; i++;
        }

        // add elements left in the second interval
        while(j <= r) {
            temp[k] = arr[j];
            k++; j++` `;
        }

        // copy temp to original interval
        for(i = l; i <= r; i += 1) {
            arr[i] = temp[i - l];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if(l < r) {
            int mid = l + (r-l) / 2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr, l, mid, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[])
    {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
