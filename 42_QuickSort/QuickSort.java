import java.util.Arrays;
import java.util.Scanner;

/**
 * QuickSort - Implementation of quick sort algorithm
 * Efficient O(n log n) sorting
 */
public class QuickSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Quick Sort ===");
        System.out.print("Enter numbers separated by spaces: ");
        String[] input = scanner.nextLine().split(" ");

        int[] arr = new int[input.length];
        for(int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        System.out.println("Original: " + Arrays.toString(arr));

        quickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted: " + Arrays.toString(arr));
        scanner.close();
    }

    private static void quickSort(int[] arr, int low, int high) {
        if(low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for(int j = low; j < high; j++) {
            if(arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
}
