import java.util.Scanner;

/**
 * TemperatureConverter - Convert between temperature units
 * Supports Celsius, Fahrenheit, and Kelvin
 */
public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Temperature Converter ===");
        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Fahrenheit to Celsius");
        System.out.println("3. Celsius to Kelvin");
        System.out.println("4. Kelvin to Celsius");
        System.out.print("Choose conversion: ");

        int choice = scanner.nextInt();
        System.out.print("Enter temperature: ");
        double temp = scanner.nextDouble();

        double result = 0;
        String from = "", to = "";

        switch(choice) {
            case 1:
                result = (temp * 9/5) + 32;
                from = "°C";
                to = "°F";
                break;
            case 2:
                result = (temp - 32) * 5/9;
                from = "°F";
                to = "°C";
                break;
            case 3:
                result = temp + 273.15;
                from = "°C";
                to = "K";
                break;
            case 4:
                result = temp - 273.15;
                from = "K";
                to = "°C";
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("%.2f%s = %.2f%s%n", temp, from, result, to);
        scanner.close();
    }
}
