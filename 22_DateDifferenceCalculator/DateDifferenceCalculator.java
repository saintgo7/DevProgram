import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

/**
 * DateDifferenceCalculator - Calculate difference between two dates
 * Shows difference in days, weeks, months, and years
 */
public class DateDifferenceCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Date Difference Calculator ===");

        System.out.println("Enter first date:");
        System.out.print("Year: ");
        int year1 = scanner.nextInt();
        System.out.print("Month: ");
        int month1 = scanner.nextInt();
        System.out.print("Day: ");
        int day1 = scanner.nextInt();

        System.out.println("\nEnter second date:");
        System.out.print("Year: ");
        int year2 = scanner.nextInt();
        System.out.print("Month: ");
        int month2 = scanner.nextInt();
        System.out.print("Day: ");
        int day2 = scanner.nextInt();

        LocalDate date1 = LocalDate.of(year1, month1, day1);
        LocalDate date2 = LocalDate.of(year2, month2, day2);

        long days = ChronoUnit.DAYS.between(date1, date2);
        long weeks = ChronoUnit.WEEKS.between(date1, date2);
        long months = ChronoUnit.MONTHS.between(date1, date2);
        long years = ChronoUnit.YEARS.between(date1, date2);

        System.out.println("\n=== Difference ===");
        System.out.println("Days: " + Math.abs(days));
        System.out.println("Weeks: " + Math.abs(weeks));
        System.out.println("Months: " + Math.abs(months));
        System.out.println("Years: " + Math.abs(years));

        scanner.close();
    }
}
