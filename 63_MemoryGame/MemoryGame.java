import java.util.*;

/**
 * MemoryGame - Match pairs of numbers
 * Test your memory!
 */
public class MemoryGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int size = 4;
        int[][] board = new int[size][size];
        boolean[][] revealed = new boolean[size][size];

        initializeBoard(board, size);

        int pairs = 0;
        int totalPairs = (size * size) / 2;
        int moves = 0;

        System.out.println("=== Memory Game ===");
        System.out.println("Match all pairs!");

        while(pairs < totalPairs) {
            printBoard(board, revealed);

            System.out.print("\nFirst card row (0-" + (size-1) + "): ");
            int r1 = scanner.nextInt();
            System.out.print("First card column (0-" + (size-1) + "): ");
            int c1 = scanner.nextInt();

            System.out.print("Second card row (0-" + (size-1) + "): ");
            int r2 = scanner.nextInt();
            System.out.print("Second card column (0-" + (size-1) + "): ");
            int c2 = scanner.nextInt();

            moves++;

            if(r1 == r2 && c1 == c2) {
                System.out.println("Same card! Try again.");
                continue;
            }

            if(revealed[r1][c1] || revealed[r2][c2]) {
                System.out.println("Card already revealed!");
                continue;
            }

            System.out.println("\nYou picked: " + board[r1][c1] + " and " + board[r2][c2]);

            if(board[r1][c1] == board[r2][c2]) {
                System.out.println("Match!");
                revealed[r1][c1] = true;
                revealed[r2][c2] = true;
                pairs++;
            } else {
                System.out.println("No match!");
            }
        }

        System.out.println("\nCongratulations! You won in " + moves + " moves!");
        scanner.close();
    }

    private static void initializeBoard(int[][] board, int size) {
        List<Integer> numbers = new ArrayList<>();
        for(int i = 1; i <= (size * size) / 2; i++) {
            numbers.add(i);
            numbers.add(i);
        }
        Collections.shuffle(numbers);

        int index = 0;
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                board[i][j] = numbers.get(index++);
            }
        }
    }

    private static void printBoard(int[][] board, boolean[][] revealed) {
        System.out.println("\n   0 1 2 3");
        for(int i = 0; i < board.length; i++) {
            System.out.print(i + " ");
            for(int j = 0; j < board[i].length; j++) {
                if(revealed[i][j]) {
                    System.out.print(" " + board[i][j]);
                } else {
                    System.out.print(" *");
                }
            }
            System.out.println();
        }
    }
}
