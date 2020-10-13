import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        if(arr[i]==arr[j]){
            return;
        }
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;
        for(int j = l;j < h;j++){
            if(arr[j] < pivot){
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack s = new Stack<Integer>();
        s.push(l);
        s.push(h);
        while(!s.isEmpty()){
            h = (int) s.pop();
            l = (int) s.pop();

            int part = partition(arr, l, h);

            if(part - 1 > l){
                s.push(l);
                s.push(part-1);
            }
            if(part + 1 < h){
                s.push(part+1);
                s.push(h);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}

// Time Complexity : O(N^2)
// Space Complexity: O(1) - as no auxillary space used except variables