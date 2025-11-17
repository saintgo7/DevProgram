import java.util.Scanner;

/**
 * PalindromeChecker - Check if string or number is palindrome
 * Works with both words and numbers
 */
public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Palindrome Checker ===");
        System.out.print("Enter text to check: ");
        String input = scanner.nextLine();

        String cleaned = input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();

        if(cleaned.equals(reversed)) {
            System.out.println("\"" + input + "\" is a palindrome!");
        } else {
            System.out.println("\"" + input + "\" is not a palindrome.");
        }

        scanner.close();
    }
}
