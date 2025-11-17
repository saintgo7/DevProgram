import java.util.Scanner;

/**
 * StringReverser - Reverse strings in various ways
 * Word-by-word, character-by-character, or sentence reversal
 */
public class StringReverser {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== String Reverser ===");
        System.out.println("1. Reverse entire string");
        System.out.println("2. Reverse word order");
        System.out.println("3. Reverse each word");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter text: ");
        String text = scanner.nextLine();

        String result = "";

        switch(choice) {
            case 1:
                result = new StringBuilder(text).reverse().toString();
                break;
            case 2:
                String[] words = text.split(" ");
                StringBuilder sb = new StringBuilder();
                for(int i = words.length - 1; i >= 0; i--) {
                    sb.append(words[i]);
                    if(i > 0) sb.append(" ");
                }
                result = sb.toString();
                break;
            case 3:
                String[] wordsToReverse = text.split(" ");
                StringBuilder sb2 = new StringBuilder();
                for(String word : wordsToReverse) {
                    sb2.append(new StringBuilder(word).reverse()).append(" ");
                }
                result = sb2.toString().trim();
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
