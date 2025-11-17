import java.util.Random;
import java.util.Scanner;

/**
 * RockPaperScissors - Classic game against computer
 * Tracks wins, losses, and ties
 */
public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int wins = 0, losses = 0, ties = 0;
        boolean playing = true;

        System.out.println("=== Rock Paper Scissors ===");

        while(playing) {
            System.out.println("\n1. Rock");
            System.out.println("2. Paper");
            System.out.println("3. Scissors");
            System.out.println("4. Quit");
            System.out.print("Choose: ");

            int choice = scanner.nextInt();
            if(choice == 4) break;
            if(choice < 1 || choice > 3) {
                System.out.println("Invalid choice!");
                continue;
            }

            int computer = random.nextInt(3) + 1;
            String[] options = {"", "Rock", "Paper", "Scissors"};

            System.out.println("You chose: " + options[choice]);
            System.out.println("Computer chose: " + options[computer]);

            if(choice == computer) {
                System.out.println("It's a tie!");
                ties++;
            } else if((choice == 1 && computer == 3) ||
                      (choice == 2 && computer == 1) ||
                      (choice == 3 && computer == 2)) {
                System.out.println("You win!");
                wins++;
            } else {
                System.out.println("You lose!");
                losses++;
            }

            System.out.printf("Score - Wins: %d, Losses: %d, Ties: %d%n", wins, losses, ties);
        }

        scanner.close();
    }
}
