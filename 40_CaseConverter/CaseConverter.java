import java.util.Scanner;

/**
 * CaseConverter - Convert text case
 * Supports uppercase, lowercase, title case, toggle case
 */
public class CaseConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Case Converter ===");
        System.out.println("1. UPPERCASE");
        System.out.println("2. lowercase");
        System.out.println("3. Title Case");
        System.out.println("4. tOGGLE cASE");
        System.out.println("5. Sentence case");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter text: ");
        String text = scanner.nextLine();

        String result = "";

        switch(choice) {
            case 1:
                result = text.toUpperCase();
                break;
            case 2:
                result = text.toLowerCase();
                break;
            case 3:
                String[] words = text.toLowerCase().split(" ");
                StringBuilder sb = new StringBuilder();
                for(String word : words) {
                    if(word.length() > 0) {
                        sb.append(Character.toUpperCase(word.charAt(0)))
                          .append(word.substring(1))
                          .append(" ");
                    }
                }
                result = sb.toString().trim();
                break;
            case 4:
                StringBuilder toggle = new StringBuilder();
                for(char c : text.toCharArray()) {
                    if(Character.isUpperCase(c)) {
                        toggle.append(Character.toLowerCase(c));
                    } else if(Character.isLowerCase(c)) {
                        toggle.append(Character.toUpperCase(c));
                    } else {
                        toggle.append(c);
                    }
                }
                result = toggle.toString();
                break;
            case 5:
                if(text.length() > 0) {
                    result = Character.toUpperCase(text.charAt(0)) + text.substring(1).toLowerCase();
                }
                break;
            default:
                System.out.println("Invalid choice!");
                scanner.close();
                return;
        }

        System.out.println("Result: " + result);
        scanner.close();
    }
}
