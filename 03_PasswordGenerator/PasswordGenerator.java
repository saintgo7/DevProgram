import java.util.Random;
import java.util.Scanner;

/**
 * PasswordGenerator - Generate secure random passwords
 * Customizable length and character types
 */
public class PasswordGenerator {
    private static final String LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
    private static final String UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String DIGITS = "0123456789";
    private static final String SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Password Generator ===");
        System.out.print("Password length: ");
        int length = scanner.nextInt();

        System.out.print("Include uppercase? (y/n): ");
        boolean useUppercase = scanner.next().toLowerCase().startsWith("y");

        System.out.print("Include numbers? (y/n): ");
        boolean useDigits = scanner.next().toLowerCase().startsWith("y");

        System.out.print("Include special characters? (y/n): ");
        boolean useSpecial = scanner.next().toLowerCase().startsWith("y");

        String characters = LOWERCASE;
        if(useUppercase) characters += UPPERCASE;
        if(useDigits) characters += DIGITS;
        if(useSpecial) characters += SPECIAL;

        StringBuilder password = new StringBuilder();
        for(int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            password.append(characters.charAt(index));
        }

        System.out.println("\nGenerated Password: " + password.toString());
        scanner.close();
    }
}
