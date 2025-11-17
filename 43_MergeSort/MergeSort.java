import java.util.Arrays;
import java.util.Scanner;

/**
 * MergeSort - Implementation of merge sort algorithm
 * Stable O(n log n) sorting algorithm
 */
public class MergeSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Merge Sort ===");
        System.out.print("Enter numbers separated by spaces: ");
        String[] input = scanner.nextLine().split(" ");

        int[] arr = new int[input.length];
        for(int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        System.out.println("Original: " + Arrays.toString(arr));

        mergeSort(arr, 0, arr.length - 1);

        System.out.println("Sorted: " + Arrays.toString(arr));
        scanner.close();
    }

    private static void mergeSort(int[] arr, int left, int right) {
        if(left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        System.arraycopy(arr, left, L, 0, n1);
        System.arraycopy(arr, mid + 1, R, 0, n2);

        int i = 0, j = 0, k = left;

        while(i < n1 && j < n2) {
            if(L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while(i < n1) arr[k++] = L[i++];
        while(j < n2) arr[k++] = R[j++];
    }
}
