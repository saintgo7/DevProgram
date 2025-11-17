import java.util.*;

/**
 * Minesweeper - Classic mine-finding game
 * Simplified text version
 */
public class Minesweeper {
    private static int[][] board;
    private static boolean[][] revealed;
    private static boolean[][] mines;
    private static final int SIZE = 5;
    private static final int NUM_MINES = 5;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        initializeGame();

        System.out.println("=== Minesweeper ===");

        while(true) {
            printBoard();
            System.out.print("Enter row and column (0-4): ");
            int r = scanner.nextInt();
            int c = scanner.nextInt();

            if(mines[r][c]) {
                System.out.println("BOOM! Game Over!");
                revealAll();
                printBoard();
                break;
            }

            reveal(r, c);

            if(checkWin()) {
                System.out.println("You Win!");
                break;
            }
        }
        scanner.close();
    }

    private static void initializeGame() {
        board = new int[SIZE][SIZE];
        revealed = new boolean[SIZE][SIZE];
        mines = new boolean[SIZE][SIZE];

        Random random = new Random();
        for(int i = 0; i < NUM_MINES; i++) {
            int r, c;
            do {
                r = random.nextInt(SIZE);
                c = random.nextInt(SIZE);
            } while(mines[r][c]);
            mines[r][c] = true;
        }

        for(int i = 0; i < SIZE; i++) {
            for(int j = 0; j < SIZE; j++) {
                if(!mines[i][j]) {
                    board[i][j] = countAdjacentMines(i, j);
                }
            }
        }
    }

    private static int countAdjacentMines(int r, int c) {
        int count = 0;
        for(int i = -1; i <= 1; i++) {
            for(int j = -1; j <= 1; j++) {
                int nr = r + i, nc = c + j;
                if(nr >= 0 && nr < SIZE && nc >= 0 && nc < SIZE && mines[nr][nc]) {
                    count++;
                }
            }
        }
        return count;
    }

    private static void reveal(int r, int c) {
        if(r < 0 || r >= SIZE || c < 0 || c >= SIZE || revealed[r][c]) return;
        revealed[r][c] = true;
        if(board[r][c] == 0) {
            for(int i = -1; i <= 1; i++) {
                for(int j = -1; j <= 1; j++) {
                    reveal(r + i, c + j);
                }
            }
        }
    }

    private static void printBoard() {
        System.out.println("\n  0 1 2 3 4");
        for(int i = 0; i < SIZE; i++) {
            System.out.print(i + " ");
            for(int j = 0; j < SIZE; j++) {
                if(revealed[i][j]) {
                    if(mines[i][j]) System.out.print("* ");
                    else System.out.print(board[i][j] + " ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    private static void revealAll() {
        for(int i = 0; i < SIZE; i++) {
            for(int j = 0; j < SIZE; j++) {
                revealed[i][j] = true;
            }
        }
    }

    private static boolean checkWin() {
        for(int i = 0; i < SIZE; i++) {
            for(int j = 0; j < SIZE; j++) {
                if(!mines[i][j] && !revealed[i][j]) return false;
            }
        }
        return true;
    }
}
