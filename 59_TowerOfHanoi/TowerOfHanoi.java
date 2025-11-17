import java.util.Scanner;

/**
 * TowerOfHanoi - Classic recursive puzzle
 * Move disks from source to destination using auxiliary peg
 */
public class TowerOfHanoi {
    private static int moves = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Tower of Hanoi ===");
        System.out.print("Enter number of disks: ");
        int n = scanner.nextInt();

        System.out.println("\nSolution:");
        hanoi(n, 'A', 'C', 'B');

        System.out.println("\nTotal moves: " + moves);
        System.out.println("Minimum moves required: " + ((int)Math.pow(2, n) - 1));

        scanner.close();
    }

    private static void hanoi(int n, char from, char to, char aux) {
        if(n == 1) {
            moves++;
            System.out.println("Move disk 1 from " + from + " to " + to);
            return;
        }

        hanoi(n-1, from, aux, to);

        moves++;
        System.out.println("Move disk " + n + " from " + from + " to " + to);

        hanoi(n-1, aux, to, from);
    }
}
