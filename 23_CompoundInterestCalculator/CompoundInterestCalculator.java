import java.util.Scanner;

/**
 * CompoundInterestCalculator - Calculate compound interest
 * Shows final amount and interest earned
 */
public class CompoundInterestCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Compound Interest Calculator ===");
        System.out.print("Principal amount: ");
        double principal = scanner.nextDouble();

        System.out.print("Annual interest rate (%): ");
        double rate = scanner.nextDouble() / 100;

        System.out.print("Time (years): ");
        int years = scanner.nextInt();

        System.out.print("Compounds per year: ");
        int n = scanner.nextInt();

        // A = P(1 + r/n)^(nt)
        double amount = principal * Math.pow(1 + rate/n, n * years);
        double interest = amount - principal;

        System.out.println("\n=== Results ===");
        System.out.printf("Principal: $%.2f%n", principal);
        System.out.printf("Interest earned: $%.2f%n", interest);
        System.out.printf("Final amount: $%.2f%n", amount);

        scanner.close();
    }
}
