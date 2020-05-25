/**
 * Time Complexity: O(n^2) 
 */

class IterativeQuickSort { 
    void swap(int arr[],int i,int j){
        int temp = arr[i]; 
        arr[i] = arr[j]; 
        arr[j] = temp;  
    }
    
    int partition(int arr[], int low, int high) 
    { 
        int pivot=arr[high];
        int i=low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                swap(arr,i,j); 
            }
        }

        swap(arr,i+1,high);
        return (i+1);
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        if (l < h) { 
            int pi = partition(arr, l, h); 
            QuickSort(arr, l, pi - 1); 
            QuickSort(arr, pi + 1, h); 
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