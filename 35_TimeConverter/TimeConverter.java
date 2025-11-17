import java.util.Scanner;

/**
 * TimeConverter - Convert between time units
 * Supports seconds, minutes, hours, days
 */
public class TimeConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Time Converter ===");
        System.out.println("1. Seconds to Minutes");
        System.out.println("2. Minutes to Hours");
        System.out.println("3. Hours to Days");
        System.out.println("4. Days to Hours");
        System.out.println("5. Hours to Minutes");
        System.out.println("6. Minutes to Seconds");
        System.out.print("Choose conversion: ");

        int choice = scanner.nextInt();
        System.out.print("Enter value: ");
        double value = scanner.nextDouble();

        double result = 0;
        String from = "", to = "";

        switch(choice) {
            case 1: result = value / 60; from = "seconds"; to = "minutes"; break;
            case 2: result = value / 60; from = "minutes"; to = "hours"; break;
            case 3: result = value / 24; from = "hours"; to = "days"; break;
            case 4: result = value * 24; from = "days"; to = "hours"; break;
            case 5: result = value * 60; from = "hours"; to = "minutes"; break;
            case 6: result = value * 60; from = "minutes"; to = "seconds"; break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("%.2f %s = %.2f %s%n", value, from, result, to);
        scanner.close();
    }
}
