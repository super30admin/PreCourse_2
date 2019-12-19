Time Complexity-Worst-O(n^2)-Average-O(nlogn)
Space Complexity-O(n)
	
package com.company;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {

        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
    }

    int partition(int arr[], int l, int h)
    {
        int pivot=h;
        int s=l;
        for(int i=l;i<pivot;i++)
        {
            if(arr[i]<arr[pivot])
            {
                if(s!=i)
                swap(arr,s,i);
                s++;
            }

        }
        swap(arr,s,pivot);
        return s;
    }


    void QuickSort(int arr[], int l, int h)
    {
        int stack[] = new int[h - l + 1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];
            int p = partition(arr, l, h);
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }
    }

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
