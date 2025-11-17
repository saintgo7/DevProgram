import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * LinearSearch - Simple sequential search
 * Finds all occurrences of target
 */
public class LinearSearch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Linear Search ===");
        System.out.print("Enter numbers separated by spaces: ");
        String[] input = scanner.nextLine().split(" ");

        int[] arr = new int[input.length];
        for(int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        System.out.println("Array: " + Arrays.toString(arr));
        System.out.print("Enter number to search: ");
        int target = scanner.nextInt();

        List<Integer> positions = linearSearch(arr, target);

        if(positions.isEmpty()) {
            System.out.println("Number not found");
        } else {
            System.out.println("Number found at positions: " + positions);
            System.out.println("Total occurrences: " + positions.size());
        }

        scanner.close();
    }

    private static List<Integer> linearSearch(int[] arr, int target) {
        List<Integer> positions = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == target) {
                positions.add(i);
            }
        }
        return positions;
    }
}
