import java.util.Arrays;
import java.util.Scanner;

/**
 * BinarySearch - Efficient search in sorted array
 * O(log n) time complexity
 */
public class BinarySearch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Binary Search ===");
        System.out.print("Enter sorted numbers separated by spaces: ");
        String[] input = scanner.nextLine().split(" ");

        int[] arr = new int[input.length];
        for(int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        System.out.println("Array: " + Arrays.toString(arr));
        System.out.print("Enter number to search: ");
        int target = scanner.nextInt();

        int result = binarySearch(arr, target);

        if(result == -1) {
            System.out.println("Number not found");
        } else {
            System.out.println("Number found at index: " + result);
        }

        scanner.close();
    }

    private static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(arr[mid] == target) {
                return mid;
            }

            if(arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}
