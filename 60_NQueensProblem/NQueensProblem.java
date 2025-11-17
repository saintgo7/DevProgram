import java.util.Scanner;

/**
 * NQueensProblem - Place N queens on NxN chessboard
 * No two queens can attack each other
 */
public class NQueensProblem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== N-Queens Problem ===");
        System.out.print("Enter board size (N): ");
        int n = scanner.nextInt();

        int[][] board = new int[n][n];

        if(solveNQueens(board, 0)) {
            System.out.println("\nSolution found:");
            printBoard(board);
        } else {
            System.out.println("\nNo solution exists!");
        }

        scanner.close();
    }

    private static boolean solveNQueens(int[][] board, int col) {
        int n = board.length;

        if(col >= n) {
            return true;
        }

        for(int row = 0; row < n; row++) {
            if(isSafe(board, row, col)) {
                board[row][col] = 1;

                if(solveNQueens(board, col + 1)) {
                    return true;
                }

                board[row][col] = 0; // Backtrack
            }
        }

        return false;
    }

    private static boolean isSafe(int[][] board, int row, int col) {
        int n = board.length;

        // Check row on left side
        for(int i = 0; i < col; i++) {
            if(board[row][i] == 1) {
                return false;
            }
        }

        // Check upper diagonal
        for(int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if(board[i][j] == 1) {
                return false;
            }
        }

        // Check lower diagonal
        for(int i = row, j = col; i < n && j >= 0; i++, j--) {
            if(board[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    private static void printBoard(int[][] board) {
        for(int[] row : board) {
            for(int cell : row) {
                System.out.print(cell == 1 ? "Q " : ". ");
            }
            System.out.println();
        }
    }
}
