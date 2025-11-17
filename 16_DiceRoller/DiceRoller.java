import java.util.Random;
import java.util.Scanner;

/**
 * DiceRoller - Roll virtual dice
 * Supports multiple dice and different sizes
 */
public class DiceRoller {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Dice Roller ===");
        System.out.print("Number of dice: ");
        int numDice = scanner.nextInt();

        System.out.print("Sides per die: ");
        int sides = scanner.nextInt();

        int total = 0;
        System.out.println("\nRolling " + numDice + "d" + sides + ":");

        for(int i = 1; i <= numDice; i++) {
            int roll = random.nextInt(sides) + 1;
            System.out.println("Die " + i + ": " + roll);
            total += roll;
        }

        System.out.println("\nTotal: " + total);
        scanner.close();
    }
}
