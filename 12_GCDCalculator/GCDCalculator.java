import java.util.Scanner;

/**
 * GCDCalculator - Calculate Greatest Common Divisor
 * Uses Euclidean algorithm
 */
public class GCDCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== GCD Calculator ===");
        System.out.print("Enter first number: ");
        int a = scanner.nextInt();

        System.out.print("Enter second number: ");
        int b = scanner.nextInt();

        int gcd = calculateGCD(Math.abs(a), Math.abs(b));
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd);

        scanner.close();
    }

    private static int calculateGCD(int a, int b) {
        while(b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
