import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * EmailValidator - Validate email addresses
 * Checks format using regex pattern
 */
public class EmailValidator {
    private static final String EMAIL_PATTERN =
        "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Email Validator ===");
        System.out.print("Enter email address: ");
        String email = scanner.nextLine();

        if(isValidEmail(email)) {
            System.out.println("✓ Valid email address");

            // Extract parts
            String[] parts = email.split("@");
            String username = parts[0];
            String domain = parts[1];

            System.out.println("Username: " + username);
            System.out.println("Domain: " + domain);
        } else {
            System.out.println("✗ Invalid email address");
            System.out.println("\nEmail must:");
            System.out.println("- Have username before @");
            System.out.println("- Have @ symbol");
            System.out.println("- Have domain after @");
            System.out.println("- Have valid TLD (e.g., .com, .org)");
        }

        scanner.close();
    }

    private static boolean isValidEmail(String email) {
        return Pattern.matches(EMAIL_PATTERN, email);
    }
}
