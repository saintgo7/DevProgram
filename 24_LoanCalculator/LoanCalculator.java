import java.util.Scanner;

/**
 * LoanCalculator - Calculate loan payments
 * Shows monthly payment, total payment, and total interest
 */
public class LoanCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Loan Calculator ===");
        System.out.print("Loan amount: ");
        double principal = scanner.nextDouble();

        System.out.print("Annual interest rate (%): ");
        double annualRate = scanner.nextDouble();

        System.out.print("Loan term (years): ");
        int years = scanner.nextInt();

        double monthlyRate = annualRate / 100 / 12;
        int months = years * 12;

        // M = P * [r(1+r)^n] / [(1+r)^n - 1]
        double monthlyPayment = principal * (monthlyRate * Math.pow(1 + monthlyRate, months))
                               / (Math.pow(1 + monthlyRate, months) - 1);

        double totalPayment = monthlyPayment * months;
        double totalInterest = totalPayment - principal;

        System.out.println("\n=== Results ===");
        System.out.printf("Monthly payment: $%.2f%n", monthlyPayment);
        System.out.printf("Total payment: $%.2f%n", totalPayment);
        System.out.printf("Total interest: $%.2f%n", totalInterest);

        scanner.close();
    }
}
