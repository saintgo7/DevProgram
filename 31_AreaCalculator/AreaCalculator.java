import java.util.Scanner;

/**
 * AreaCalculator - Calculate area of various shapes
 * Supports circle, rectangle, triangle, square
 */
public class AreaCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Area Calculator ===");
        System.out.println("1. Circle");
        System.out.println("2. Rectangle");
        System.out.println("3. Triangle");
        System.out.println("4. Square");
        System.out.print("Choose shape: ");

        int choice = scanner.nextInt();
        double area = 0;

        switch(choice) {
            case 1:
                System.out.print("Enter radius: ");
                double radius = scanner.nextDouble();
                area = Math.PI * radius * radius;
                break;
            case 2:
                System.out.print("Enter length: ");
                double length = scanner.nextDouble();
                System.out.print("Enter width: ");
                double width = scanner.nextDouble();
                area = length * width;
                break;
            case 3:
                System.out.print("Enter base: ");
                double base = scanner.nextDouble();
                System.out.print("Enter height: ");
                double height = scanner.nextDouble();
                area = 0.5 * base * height;
                break;
            case 4:
                System.out.print("Enter side: ");
                double side = scanner.nextDouble();
                area = side * side;
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("Area: %.2f%n", area);
        scanner.close();
    }
}
