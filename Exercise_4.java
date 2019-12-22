class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		int s1 = m - l + 1;
		int s2 = r - m;

		// initialize array from low to mid for storing left half elements
		int[] left = new int[s1];
		// initialize array from mid+1 to right for storing right half elements
		int[] right = new int[s2];

		// fill elements in left and right array from original array
		for (int i = 0; i < s1; i++) {
			left[i] = arr[l + i];
		}

		for (int j = 0; j < s2; j++) {
			right[j] = arr[m + 1 + j];
		}

		int i = 0, j = 0, k = l;
		// check from both subarrays, when we get small element, merge it to bigger
		// array
		while (i < s1 && j < s2) {
			if (left[i] <= right[j]) {
				arr[k] = left[i];
				i++;
			} else {
				arr[k] = right[j];
				j++;
			}
			k++;
		}

		// add remaining elements from left subarray if exist
		while (i < s1) {
			arr[k] = left[i];
			i++;
			k++;
		}
		// add remaining elements from right subarray if exist
		while (i < s2) {
			arr[k] = right[j];
			j++;
			k++;
		}

	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		// Write your code here
		// Call mergeSort from here
		// sort array until left index becomes greater than right index
		if (l < r) {
			int m = (l + r) / 2;
			// sort left half
			sort(arr, l, m);
			// sort right half
			sort(arr, m + 1, r);
			// after sorting merge them
			merge(arr, l, m, r);
		}

	}

	/* A utility function to print array of size n */
	static void printArray(int arr[]) {
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver method
	public static void main(String args[]) {
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}