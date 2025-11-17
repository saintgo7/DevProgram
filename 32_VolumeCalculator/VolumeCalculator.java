import java.util.Scanner;

/**
 * VolumeCalculator - Calculate volume of 3D shapes
 * Supports sphere, cube, cylinder, cone
 */
public class VolumeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Volume Calculator ===");
        System.out.println("1. Sphere");
        System.out.println("2. Cube");
        System.out.println("3. Cylinder");
        System.out.println("4. Cone");
        System.out.print("Choose shape: ");

        int choice = scanner.nextInt();
        double volume = 0;

        switch(choice) {
            case 1:
                System.out.print("Enter radius: ");
                double radius = scanner.nextDouble();
                volume = (4.0/3.0) * Math.PI * Math.pow(radius, 3);
                break;
            case 2:
                System.out.print("Enter side: ");
                double side = scanner.nextDouble();
                volume = Math.pow(side, 3);
                break;
            case 3:
                System.out.print("Enter radius: ");
                double r = scanner.nextDouble();
                System.out.print("Enter height: ");
                double h = scanner.nextDouble();
                volume = Math.PI * r * r * h;
                break;
            case 4:
                System.out.print("Enter radius: ");
                double rad = scanner.nextDouble();
                System.out.print("Enter height: ");
                double height = scanner.nextDouble();
                volume = (1.0/3.0) * Math.PI * rad * rad * height;
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.printf("Volume: %.2f%n", volume);
        scanner.close();
    }
}
