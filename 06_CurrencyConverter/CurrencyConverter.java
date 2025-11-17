import java.util.Scanner;

/**
 * CurrencyConverter - Convert between major currencies
 * Uses fixed exchange rates (for demonstration)
 */
public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Exchange rates (to USD)
        final double EUR_TO_USD = 1.09;
        final double GBP_TO_USD = 1.27;
        final double JPY_TO_USD = 0.0067;
        final double KRW_TO_USD = 0.00075;

        System.out.println("=== Currency Converter ===");
        System.out.println("1. EUR to USD");
        System.out.println("2. GBP to USD");
        System.out.println("3. JPY to USD");
        System.out.println("4. KRW to USD");
        System.out.println("5. USD to EUR");
        System.out.println("6. USD to GBP");
        System.out.println("7. USD to JPY");
        System.out.println("8. USD to KRW");
        System.out.print("Choose conversion: ");

        int choice = scanner.nextInt();
        System.out.print("Enter amount: ");
        double amount = scanner.nextDouble();

        double result = 0;
        String from = "", to = "";

        switch(choice) {
            case 1: result = amount * EUR_TO_USD; from = "EUR"; to = "USD"; break;
            case 2: result = amount * GBP_TO_USD; from = "GBP"; to = "USD"; break;
            case 3: result = amount * JPY_TO_USD; from = "JPY"; to = "USD"; break;
            case 4: result = amount * KRW_TO_USD; from = "KRW"; to = "USD"; break;
            case 5: result = amount / EUR_TO_USD; from = "USD"; to = "EUR"; break;
            case 6: result = amount / GBP_TO_USD; from = "USD"; to = "GBP"; break;
            case 7: result = amount / JPY_TO_USD; from = "USD"; to = "JPY"; break;
            case 8: result = amount / KRW_TO_USD; from = "USD"; to = "KRW"; break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("%.2f %s = %.2f %s%n", amount, from, result, to);
        scanner.close();
    }
}
