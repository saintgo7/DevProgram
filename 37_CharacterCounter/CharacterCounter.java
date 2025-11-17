import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * CharacterCounter - Count frequency of each character
 * Shows character distribution in text
 */
public class CharacterCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Character Counter ===");
        System.out.print("Enter text: ");
        String text = scanner.nextLine();

        Map<Character, Integer> frequency = new HashMap<>();

        for(char c : text.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        System.out.println("\n=== Character Frequency ===");
        frequency.entrySet().stream()
            .sorted((a, b) -> b.getValue().compareTo(a.getValue()))
            .forEach(entry -> {
                char c = entry.getKey();
                String display = c == ' ' ? "SPACE" :
                                c == '\n' ? "NEWLINE" :
                                c == '\t' ? "TAB" :
                                String.valueOf(c);
                System.out.printf("'%s': %d%n", display, entry.getValue());
            });

        scanner.close();
    }
}
