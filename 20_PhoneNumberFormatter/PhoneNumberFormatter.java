import java.util.Scanner;

/**
 * PhoneNumberFormatter - Format phone numbers
 * Supports various input formats and outputs clean format
 */
public class PhoneNumberFormatter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Phone Number Formatter ===");
        System.out.print("Enter phone number: ");
        String input = scanner.nextLine();

        // Remove all non-digit characters
        String digits = input.replaceAll("\\D", "");

        if(digits.length() == 10) {
            // Format as (XXX) XXX-XXXX
            String formatted = String.format("(%s) %s-%s",
                digits.substring(0, 3),
                digits.substring(3, 6),
                digits.substring(6));
            System.out.println("Formatted: " + formatted);
        } else if(digits.length() == 11 && digits.startsWith("1")) {
            // Format as +1 (XXX) XXX-XXXX
            String formatted = String.format("+1 (%s) %s-%s",
                digits.substring(1, 4),
                digits.substring(4, 7),
                digits.substring(7));
            System.out.println("Formatted: " + formatted);
        } else {
            System.out.println("Invalid phone number!");
            System.out.println("Enter 10 digits or 11 digits starting with 1");
        }

        scanner.close();
    }
}
