import java.time.LocalDate;
import java.time.Period;
import java.util.Scanner;

/**
 * AgeCalculator - Calculate age from birthdate
 * Shows years, months, and days
 */
public class AgeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Age Calculator ===");
        System.out.print("Enter birth year: ");
        int year = scanner.nextInt();

        System.out.print("Enter birth month (1-12): ");
        int month = scanner.nextInt();

        System.out.print("Enter birth day: ");
        int day = scanner.nextInt();

        LocalDate birthDate = LocalDate.of(year, month, day);
        LocalDate today = LocalDate.now();

        Period period = Period.between(birthDate, today);

        System.out.println("\nYou are:");
        System.out.println(period.getYears() + " years");
        System.out.println(period.getMonths() + " months");
        System.out.println(period.getDays() + " days old");

        System.out.println("\nTotal days: " + birthDate.until(today).getDays());

        scanner.close();
    }
}
