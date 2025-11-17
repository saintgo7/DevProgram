import java.util.Random;
import java.util.Scanner;

/**
 * NumberGuessingGame - Guess the random number
 * Provides hints (higher/lower) for each guess
 */
public class NumberGuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Number Guessing Game ===");
        System.out.print("Enter range (1 to N): ");
        int max = scanner.nextInt();

        int target = random.nextInt(max) + 1;
        int attempts = 0;
        boolean won = false;

        System.out.println("I'm thinking of a number between 1 and " + max);

        while(!won) {
            System.out.print("Your guess: ");
            int guess = scanner.nextInt();
            attempts++;

            if(guess == target) {
                won = true;
                System.out.println("Congratulations! You found it in " + attempts + " attempts!");
            } else if(guess < target) {
                System.out.println("Too low! Try again.");
            } else {
                System.out.println("Too high! Try again.");
            }
        }

        scanner.close();
    }
}
