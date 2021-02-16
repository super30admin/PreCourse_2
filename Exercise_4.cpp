#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 

// Time Complexity: O(nlogn)
// Space Complexity: O(n)
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int len1 = m-l+1;
    int len2 = r-m;
    int left[len1];int right[len2];
    for(int i = 0; i < len1;i++)left[i]=arr[l+i];
    for(int j = 0; j < len2;j++)right[j]=arr[m+1+j];
    int i=0,j=0,k=l;
    while(i < len1 && j < len2){
        if(left[i]<=right[j])arr[k++] = left[i++];
        else arr[k++] = right[j++];
    }
    while(i < len1)arr[k++] = left[i++];
    while(j < len2)arr[k++] = right[j++];
    

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(r > l){
        int m = l + (r-l)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);


    }
} 
  
/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 
  
/* Driver program to test above functions */
int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}