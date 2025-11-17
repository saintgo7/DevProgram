import java.util.Scanner;

/**
 * Calculator - Basic arithmetic calculator
 * Performs addition, subtraction, multiplication, and division
 */
public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Calculator ===");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.print("Choose operation (1-4): ");

        int choice = scanner.nextInt();

        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        double result = 0;
        String operation = "";

        switch(choice) {
            case 1:
                result = num1 + num2;
                operation = "+";
                break;
            case 2:
                result = num1 - num2;
                operation = "-";
                break;
            case 3:
                result = num1 * num2;
                operation = "*";
                break;
            case 4:
                if(num2 != 0) {
                    result = num1 / num2;
                    operation = "/";
                } else {
                    System.out.println("Error: Division by zero!");
                    scanner.close();
                    return;
                }
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("Result: %.2f %s %.2f = %.2f%n", num1, operation, num2, result);
        scanner.close();
    }
}
