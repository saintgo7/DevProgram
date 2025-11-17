import java.util.Scanner;

/**
 * KnapsackProblem - 0/1 Knapsack using dynamic programming
 * Maximize value within weight constraint
 */
public class KnapsackProblem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== 0/1 Knapsack Problem ===");
        System.out.print("Enter number of items: ");
        int n = scanner.nextInt();

        int[] weights = new int[n];
        int[] values = new int[n];

        System.out.println("Enter weights:");
        for(int i = 0; i < n; i++) {
            weights[i] = scanner.nextInt();
        }

        System.out.println("Enter values:");
        for(int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = scanner.nextInt();

        int maxValue = knapsack(weights, values, capacity);
        System.out.println("\nMaximum value: " + maxValue);

        scanner.close();
    }

    private static int knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for(int i = 1; i <= n; i++) {
            for(int w = 1; w <= capacity; w++) {
                if(weights[i-1] <= w) {
                    dp[i][w] = Math.max(
                        values[i-1] + dp[i-1][w - weights[i-1]],
                        dp[i-1][w]
                    );
                } else {
                    dp[i][w] = dp[i-1][w];
                }
            }
        }

        return dp[n][capacity];
    }
}
