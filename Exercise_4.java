// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :

public class RecSort {
	public static void main(String args[])
	{
		int arr[]= {5,7,1,2,4};
		int ans[]=mergeSort(arr,0,arr.length-1);
		for(int index:ans)
		{
			System.out.println("Val"+index);
		}
	}
public static int[] mergeSort(int arr[],int lo,int hi)
	{
		if(lo==hi)
		{
			int[] base=new int[1];
			base[0]=arr[lo];
			return base;
			
		}
		int mid=(lo+hi)/2;
		int f[]=mergeSort(arr,lo,mid);
		int h[]=mergeSort(arr,mid+1,hi);
		
		int merge[]=mergeJoin(f,h);
		return merge;
	}
}
