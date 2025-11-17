import java.util.Scanner;

/**
 * PercentageCalculator - Various percentage calculations
 * Includes percentage of number, percentage increase/decrease
 */
public class PercentageCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Percentage Calculator ===");
        System.out.println("1. What is X% of Y?");
        System.out.println("2. X is what % of Y?");
        System.out.println("3. Percentage increase/decrease");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();

        if(choice == 1) {
            System.out.print("Enter percentage: ");
            double percent = scanner.nextDouble();
            System.out.print("Enter number: ");
            double number = scanner.nextDouble();
            double result = (percent / 100) * number;
            System.out.printf("%.2f%% of %.2f = %.2f%n", percent, number, result);
        } else if(choice == 2) {
            System.out.print("Enter first number: ");
            double num1 = scanner.nextDouble();
            System.out.print("Enter second number: ");
            double num2 = scanner.nextDouble();
            double percent = (num1 / num2) * 100;
            System.out.printf("%.2f is %.2f%% of %.2f%n", num1, percent, num2);
        } else if(choice == 3) {
            System.out.print("Enter original value: ");
            double original = scanner.nextDouble();
            System.out.print("Enter new value: ");
            double newValue = scanner.nextDouble();
            double change = ((newValue - original) / original) * 100;
            if(change > 0) {
                System.out.printf("Percentage increase: %.2f%%%n", change);
            } else {
                System.out.printf("Percentage decrease: %.2f%%%n", Math.abs(change));
            }
        }

        scanner.close();
    }
}
