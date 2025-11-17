import java.util.Scanner;

/**
 * UnitConverter - Convert between various units
 * Length, weight, and volume conversions
 */
public class UnitConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Unit Converter ===");
        System.out.println("1. Kilometers to Miles");
        System.out.println("2. Miles to Kilometers");
        System.out.println("3. Kilograms to Pounds");
        System.out.println("4. Pounds to Kilograms");
        System.out.println("5. Liters to Gallons");
        System.out.println("6. Gallons to Liters");
        System.out.print("Choose conversion: ");

        int choice = scanner.nextInt();
        System.out.print("Enter value: ");
        double value = scanner.nextDouble();

        double result = 0;
        String from = "", to = "";

        switch(choice) {
            case 1: result = value * 0.621371; from = "km"; to = "miles"; break;
            case 2: result = value * 1.60934; from = "miles"; to = "km"; break;
            case 3: result = value * 2.20462; from = "kg"; to = "lbs"; break;
            case 4: result = value * 0.453592; from = "lbs"; to = "kg"; break;
            case 5: result = value * 0.264172; from = "L"; to = "gal"; break;
            case 6: result = value * 3.78541; from = "gal"; to = "L"; break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("%.2f %s = %.2f %s%n", value, from, result, to);
        scanner.close();
    }
}
