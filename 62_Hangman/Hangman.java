import java.util.*;

/**
 * Hangman - Classic word guessing game
 * Guess the word letter by letter
 */
public class Hangman {
    private static final String[] WORDS = {
        "java", "programming", "computer", "algorithm", "developer",
        "software", "hardware", "database", "network", "security"
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String word = WORDS[random.nextInt(WORDS.length)];
        char[] guessed = new char[word.length()];
        Arrays.fill(guessed, '_');

        Set<Character> usedLetters = new HashSet<>();
        int attemptsLeft = 6;

        System.out.println("=== Hangman ===");

        while(attemptsLeft > 0 && new String(guessed).contains("_")) {
            System.out.println("\nWord: " + String.valueOf(guessed));
            System.out.println("Attempts left: " + attemptsLeft);
            System.out.println("Used letters: " + usedLetters);

            System.out.print("Guess a letter: ");
            char guess = scanner.next().toLowerCase().charAt(0);

            if(usedLetters.contains(guess)) {
                System.out.println("Already guessed!");
                continue;
            }

            usedLetters.add(guess);

            boolean found = false;
            for(int i = 0; i < word.length(); i++) {
                if(word.charAt(i) == guess) {
                    guessed[i] = guess;
                    found = true;
                }
            }

            if(!found) {
                attemptsLeft--;
                System.out.println("Wrong guess!");
            } else {
                System.out.println("Correct!");
            }
        }

        if(!new String(guessed).contains("_")) {
            System.out.println("\nYou won! The word was: " + word);
        } else {
            System.out.println("\nYou lost! The word was: " + word);
        }

        scanner.close();
    }
}
