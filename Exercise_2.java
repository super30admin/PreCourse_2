// Time Complexity :O(nlogn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :

public class RecSort {
	public static void main(String args[])
	{
		int arr[]= {5,7,1,2,4};
		quickSort(arr,0,arr.length-1);
		for(int index:arr)
		{
			System.out.println("Val"+index);
		}
	}
public static void quickSort(int arr[],int lo,int hi)
	{
		if(lo>=hi)
		{
			return;
		}
		int mid=(lo+hi)/2;
		int pivot=arr[mid];
		int left=lo;
		int right=hi;
		while(left<=right)
		{
			while(arr[left]<pivot)
			{
				left++;
			}
			while(arr[right]>pivot)
			{
				right--;
			}
			if(left<=right)
			{
			
				int temp=arr[left];
				arr[left]=arr[right];
				arr[right]=temp;
				left++;
				right--;
			}
			
		}
		// Small problem
		quickSort(arr,lo,right);
		quickSort(arr,left,hi);
	}
}
