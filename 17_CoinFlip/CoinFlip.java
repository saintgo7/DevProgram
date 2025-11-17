import java.util.Random;
import java.util.Scanner;

/**
 * CoinFlip - Flip a virtual coin
 * Track statistics for multiple flips
 */
public class CoinFlip {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Coin Flip ===");
        System.out.print("How many times to flip? ");
        int flips = scanner.nextInt();

        int heads = 0, tails = 0;

        for(int i = 1; i <= flips; i++) {
            boolean isHeads = random.nextBoolean();
            String result = isHeads ? "Heads" : "Tails";

            if(flips <= 10) {
                System.out.println("Flip " + i + ": " + result);
            }

            if(isHeads) heads++;
            else tails++;
        }

        System.out.println("\n=== Results ===");
        System.out.println("Heads: " + heads + " (" + (heads * 100.0 / flips) + "%)");
        System.out.println("Tails: " + tails + " (" + (tails * 100.0 / flips) + "%)");

        scanner.close();
    }
}
