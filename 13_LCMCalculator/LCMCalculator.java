import java.util.Scanner;

/**
 * LCMCalculator - Calculate Least Common Multiple
 * Uses GCD to calculate LCM
 */
public class LCMCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== LCM Calculator ===");
        System.out.print("Enter first number: ");
        int a = scanner.nextInt();

        System.out.print("Enter second number: ");
        int b = scanner.nextInt();

        int lcm = calculateLCM(Math.abs(a), Math.abs(b));
        System.out.println("LCM of " + a + " and " + b + " is: " + lcm);

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

    private static int calculateLCM(int a, int b) {
        return (a * b) / calculateGCD(a, b);
    }
}
