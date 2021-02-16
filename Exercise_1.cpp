#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 

//Time Complexity -> O(log(n)) Everytime we are dividing our search in half.
//Space Complexity -> O(log(n)) For the recursive stack.
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if(r >=l){
    int mid = l + (r-l)/2;
    if(x==arr[mid])return mid;
    else if(x<arr[mid]) return binarySearch(arr,l,mid-1,x);
    else return binarySearch(arr,mid+1,r,x);
    }
    return -1;
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 40; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", 
                            result); 
    return 0; 
} 
