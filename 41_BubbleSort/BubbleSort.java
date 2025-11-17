import java.util.Arrays;
import java.util.Scanner;

/**
 * BubbleSort - Implementation of bubble sort algorithm
 * Shows step-by-step sorting process
 */
public class BubbleSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Bubble Sort ===");
        System.out.print("Enter numbers separated by spaces: ");
        String[] input = scanner.nextLine().split(" ");

        int[] arr = new int[input.length];
        for(int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        System.out.println("Original: " + Arrays.toString(arr));

        bubbleSort(arr);

        System.out.println("Sorted: " + Arrays.toString(arr));
        scanner.close();
    }

    private static void bubbleSort(int[] arr) {
        int n = arr.length;
        for(int i = 0; i < n-1; i++) {
            boolean swapped = false;
            for(int j = 0; j < n-i-1; j++) {
                if(arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if(!swapped) break;
        }
    }
}
