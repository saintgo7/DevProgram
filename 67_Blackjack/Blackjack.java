import java.util.*;

/**
 * Blackjack - Card game against dealer
 * Try to get 21 without going over
 */
public class Blackjack {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Blackjack ===");

        int playerTotal = drawCard(random) + drawCard(random);
        int dealerTotal = drawCard(random) + drawCard(random);

        System.out.println("Your cards total: " + playerTotal);
        System.out.println("Dealer showing: " + (dealerTotal > 21 ? 21 : dealerTotal / 2));

        while(playerTotal < 21) {
            System.out.print("Hit or Stand? (h/s): ");
            String choice = scanner.nextLine().toLowerCase();

            if(choice.equals("h")) {
                int card = drawCard(random);
                playerTotal += card;
                System.out.println("Drew: " + card + ", Total: " + playerTotal);
            } else {
                break;
            }
        }

        if(playerTotal > 21) {
            System.out.println("Bust! You lose!");
        } else {
            while(dealerTotal < 17) {
                dealerTotal += drawCard(random);
            }

            System.out.println("\nYour total: " + playerTotal);
            System.out.println("Dealer total: " + dealerTotal);

            if(dealerTotal > 21 || playerTotal > dealerTotal) {
                System.out.println("You win!");
            } else if(playerTotal == dealerTotal) {
                System.out.println("Push (tie)!");
            } else {
                System.out.println("Dealer wins!");
            }
        }

        scanner.close();
    }

    private static int drawCard(Random random) {
        int card = random.nextInt(13) + 1;
        return card > 10 ? 10 : card;
    }
}
