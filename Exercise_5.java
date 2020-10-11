// Time Complexity :O(nlogn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :

public class Demo{
   void swap_vals(int arr[], int i, int j){
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
   }
   int partition(int arr[], int l, int h){
      int x = arr[h];
      int i = (l - 1);
      for (int j = l; j <= h - 1; j++){
         if (arr[j] <= x){
            i++;
            swap_vals(arr, i, j);
         }
      }
      swap_vals(arr, i + 1, h);
      return (i + 1);
   }
   void quick_sort(int arr[], int l, int h){
      int my_list[] = new int[h - l + 1];
      int top = -1;
      my_list[++top] = l;
      my_list[++top] = h;
      while (top >= 0){
         h = my_list[top--];
         l = my_list[top--];
         int p = partition(arr, l, h);
         if (p - 1 > l){
            my_list[++top] = l;
            my_list[++top] = p - 1;
         }  
         if (p + 1 < h){
            my_list[++top] = p + 1;
            my_list[++top] = h;
         }
      }
   }
   public static void main(String args[]){
      Demo my_ob = new Demo();
      int my_arr[] = { 34, 76, 41, 32, 11, 0 , 91, 102, -11};
      my_ob.quick_sort(my_arr, 0, my_arr.length - 1);
      int i;
      System.out.println("After iteratively performing quick sort, the array is ");
      for (i = 0; i < my_arr.length; ++i)
      System.out.print(my_arr[i] + " ");
   }
}
