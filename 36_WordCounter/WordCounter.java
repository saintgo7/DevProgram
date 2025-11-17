import java.util.Scanner;

/**
 * WordCounter - Count words, characters, sentences
 * Provides detailed text statistics
 */
public class WordCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Word Counter ===");
        System.out.println("Enter text (type 'END' on new line when done):");

        StringBuilder text = new StringBuilder();
        String line;
        while(!(line = scanner.nextLine()).equals("END")) {
            text.append(line).append(" ");
        }

        String input = text.toString().trim();

        // Count statistics
        int words = input.isEmpty() ? 0 : input.split("\\s+").length;
        int characters = input.length();
        int charactersNoSpaces = input.replaceAll("\\s", "").length();
        int sentences = input.split("[.!?]+").length;
        int paragraphs = input.split("\n\n+").length;

        System.out.println("\n=== Statistics ===");
        System.out.println("Words: " + words);
        System.out.println("Characters (with spaces): " + characters);
        System.out.println("Characters (no spaces): " + charactersNoSpaces);
        System.out.println("Sentences: " + sentences);
        System.out.println("Paragraphs: " + paragraphs);

        if(words > 0) {
            System.out.printf("Average word length: %.2f%n", (double)charactersNoSpaces / words);
        }

        scanner.close();
    }
}
