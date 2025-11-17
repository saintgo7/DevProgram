import java.util.Scanner;

/**
 * PasswordStrengthChecker - Evaluate password security
 * Checks length, complexity, and provides recommendations
 */
public class PasswordStrengthChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Password Strength Checker ===");
        System.out.print("Enter password to check: ");
        String password = scanner.nextLine();

        int score = 0;
        StringBuilder feedback = new StringBuilder();

        // Length check
        if(password.length() >= 8) score++;
        else feedback.append("- Use at least 8 characters\n");

        if(password.length() >= 12) score++;

        // Complexity checks
        if(password.matches(".*[a-z].*")) score++;
        else feedback.append("- Add lowercase letters\n");

        if(password.matches(".*[A-Z].*")) score++;
        else feedback.append("- Add uppercase letters\n");

        if(password.matches(".*\\d.*")) score++;
        else feedback.append("- Add numbers\n");

        if(password.matches(".*[!@#$%^&*()\\-_=+\\[\\]{}|;:,.<>?].*")) score++;
        else feedback.append("- Add special characters\n");

        // Determine strength
        String strength;
        if(score <= 2) strength = "Weak";
        else if(score <= 4) strength = "Medium";
        else strength = "Strong";

        System.out.println("\nPassword Strength: " + strength);
        System.out.println("Score: " + score + "/6");

        if(feedback.length() > 0) {
            System.out.println("\nRecommendations:");
            System.out.print(feedback.toString());
        }

        scanner.close();
    }
}
