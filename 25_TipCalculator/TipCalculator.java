import java.util.Scanner;

/**
 * TipCalculator - Calculate tip and split bill
 * Supports custom tip percentages and bill splitting
 */
public class TipCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Tip Calculator ===");
        System.out.print("Bill amount: $");
        double bill = scanner.nextDouble();

        System.out.print("Tip percentage (e.g., 15, 18, 20): ");
        double tipPercent = scanner.nextDouble();

        System.out.print("Number of people: ");
        int people = scanner.nextInt();

        double tipAmount = bill * (tipPercent / 100);
        double total = bill + tipAmount;
        double perPerson = total / people;

        System.out.println("\n=== Results ===");
        System.out.printf("Bill amount: $%.2f%n", bill);
        System.out.printf("Tip (%%.0f%%): $%.2f%n", tipPercent, tipAmount);
        System.out.printf("Total: $%.2f%n", total);
        System.out.printf("Per person: $%.2f%n", perPerson);

        scanner.close();
    }
}
