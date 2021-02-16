#include <iostream> 
#include<stack>
using namespace std; 
// Time Complexity: O(n*n)
// Space Complexity: O(n)
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int low, int high) 
{  
    //Your Code here 
    int pivot = arr[high];
    int i = low-1;
    for(int j = low; j < high ;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
        swap(arr[i+1],arr[high]);
        return i+1;
}  
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int>st;
    st.push(l);st.push(h);
    while(!st.empty()){
        h =st.top();st.pop();
        l =st.top();st.pop();
        int p = partition(arr,l,h);
        if(p-1>l){
            st.push(l);
            st.push(p-1);
        }
        if(p+1<h){
            st.push(p+1);
            st.push(h);
        }

    }
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
    cout << endl;
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    printArr(arr, n); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 