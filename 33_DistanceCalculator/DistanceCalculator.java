import java.util.Scanner;

/**
 * DistanceCalculator - Calculate distance between two points
 * Supports 2D and 3D coordinates
 */
public class DistanceCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Distance Calculator ===");
        System.out.println("1. 2D Distance");
        System.out.println("2. 3D Distance");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();

        if(choice == 1) {
            System.out.println("Enter first point (x1, y1):");
            System.out.print("x1: ");
            double x1 = scanner.nextDouble();
            System.out.print("y1: ");
            double y1 = scanner.nextDouble();

            System.out.println("Enter second point (x2, y2):");
            System.out.print("x2: ");
            double x2 = scanner.nextDouble();
            System.out.print("y2: ");
            double y2 = scanner.nextDouble();

            double distance = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
            System.out.printf("Distance: %.2f%n", distance);

        } else if(choice == 2) {
            System.out.println("Enter first point (x1, y1, z1):");
            System.out.print("x1: ");
            double x1 = scanner.nextDouble();
            System.out.print("y1: ");
            double y1 = scanner.nextDouble();
            System.out.print("z1: ");
            double z1 = scanner.nextDouble();

            System.out.println("Enter second point (x2, y2, z2):");
            System.out.print("x2: ");
            double x2 = scanner.nextDouble();
            System.out.print("y2: ");
            double y2 = scanner.nextDouble();
            System.out.print("z2: ");
            double z2 = scanner.nextDouble();

            double distance = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2) + Math.pow(z2-z1, 2));
            System.out.printf("Distance: %.2f%n", distance);
        }

        scanner.close();
    }
}
