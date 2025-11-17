import java.util.Scanner;

/**
 * FibonacciGenerator - Generate Fibonacci sequence
 * Shows first N Fibonacci numbers
 */
public class FibonacciGenerator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Fibonacci Generator ===");
        System.out.print("How many Fibonacci numbers to generate? ");
        int n = scanner.nextInt();

        System.out.println("\nFirst " + n + " Fibonacci numbers:");

        long a = 0, b = 1;
        for(int i = 1; i <= n; i++) {
            System.out.print(a + " ");
            long temp = a + b;
            a = b;
            b = temp;
        }
        System.out.println();

        scanner.close();
    }
}
