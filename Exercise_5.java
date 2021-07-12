import java.util.*;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	    arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int piv = l;
        int s = l + 1, e = h;

        while(s <= e)
        {
            if(arr[s] <= arr[piv])
            {
                s++;
            }
            else if(arr[e] >= arr[piv])
            {
                e--;
            }
            else 
            {
                swap(arr, s, e);
                s++;
                e--;
            }
        }

        swap(arr, s - 1, piv);
        return s - 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    // TC: O(N Lg N). (N ^ 2) In worst case
    // SC: O(Lg N).. For Stack
    void QuickSort(int arr[], int l, int h) 
    { 
       Stack<int[]> st = new Stack<>();
       int[] init = {l, h};
       
       st.push(init);

       while(!st.isEmpty())
       {
           int[] state = st.pop();
           int low = state[0];
           int high = state[1];
           if(low < high)
           {
               int pi = partition(arr, low, high);
               int[] leftState = {low, pi - 1};
               int[] rightState = {pi + 1, high};
               st.push(rightState);
               st.push(leftState);
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
        System.out.println("");
    } 
} 