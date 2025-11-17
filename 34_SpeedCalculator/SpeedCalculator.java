import java.util.Scanner;

/**
 * SpeedCalculator - Calculate speed, distance, or time
 * Uses formula: Speed = Distance / Time
 */
public class SpeedCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Speed Calculator ===");
        System.out.println("1. Calculate Speed");
        System.out.println("2. Calculate Distance");
        System.out.println("3. Calculate Time");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();

        if(choice == 1) {
            System.out.print("Enter distance (km): ");
            double distance = scanner.nextDouble();
            System.out.print("Enter time (hours): ");
            double time = scanner.nextDouble();
            double speed = distance / time;
            System.out.printf("Speed: %.2f km/h%n", speed);
        } else if(choice == 2) {
            System.out.print("Enter speed (km/h): ");
            double speed = scanner.nextDouble();
            System.out.print("Enter time (hours): ");
            double time = scanner.nextDouble();
            double distance = speed * time;
            System.out.printf("Distance: %.2f km%n", distance);
        } else if(choice == 3) {
            System.out.print("Enter distance (km): ");
            double distance = scanner.nextDouble();
            System.out.print("Enter speed (km/h): ");
            double speed = scanner.nextDouble();
            double time = distance / speed;
            System.out.printf("Time: %.2f hours%n", time);
        }

        scanner.close();
    }
}
