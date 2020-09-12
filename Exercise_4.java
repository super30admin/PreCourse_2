//Time Complexity: O(nlogn)
//Space Complexity: O(n)

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        int l1 = m-l+1;
        int r1 = r-m;
        int[] left = new int[l1];
        int[] right = new int[r1];
        for(int i=0;i<l1;++i){
            left[i]=arr[1+i];
        }
        for(int j=0;j<r1;++j){
            right[j]=arr[m+1+j];
        }
        int i=0, j=0;
        int k=1;
        while(i<l1 && j<r1){
            if(left[i]>=right[j]){
                arr[k++] = right[j++];
            }else{
                arr[k++] = left[i++];
            }
        }
        while(i<l1){
            arr[k++] = left[i++];
        }
        while(j<r1){
            arr[k++] = right[j++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here
        if(l<r) {
            int m = (l+r)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
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
        int arr[] = {12, 11, 13, 15, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 