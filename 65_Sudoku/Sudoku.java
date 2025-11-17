import java.util.Scanner;

/**
 * Sudoku - Sudoku puzzle solver
 * Uses backtracking algorithm
 */
public class Sudoku {
    private static final int SIZE = 9;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] board = {
            {5,3,0,0,7,0,0,0,0},
            {6,0,0,1,9,5,0,0,0},
            {0,9,8,0,0,0,0,6,0},
            {8,0,0,0,6,0,0,0,3},
            {4,0,0,8,0,3,0,0,1},
            {7,0,0,0,2,0,0,0,6},
            {0,6,0,0,0,0,2,8,0},
            {0,0,0,4,1,9,0,0,5},
            {0,0,0,0,8,0,0,7,9}
        };

        System.out.println("=== Sudoku Solver ===");
        System.out.println("\nPuzzle:");
        printBoard(board);

        if(solveSudoku(board)) {
            System.out.println("\nSolution:");
            printBoard(board);
        } else {
            System.out.println("\nNo solution exists!");
        }

        scanner.close();
    }

    private static boolean solveSudoku(int[][] board) {
        for(int row = 0; row < SIZE; row++) {
            for(int col = 0; col < SIZE; col++) {
                if(board[row][col] == 0) {
                    for(int num = 1; num <= 9; num++) {
                        if(isValid(board, row, col, num)) {
                            board[row][col] = num;

                            if(solveSudoku(board)) {
                                return true;
                            }

                            board[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isValid(int[][] board, int row, int col, int num) {
        for(int i = 0; i < SIZE; i++) {
            if(board[row][i] == num) return false;
        }

        for(int i = 0; i < SIZE; i++) {
            if(board[i][col] == num) return false;
        }

        int boxRow = row - row % 3;
        int boxCol = col - col % 3;
        for(int i = boxRow; i < boxRow + 3; i++) {
            for(int j = boxCol; j < boxCol + 3; j++) {
                if(board[i][j] == num) return false;
            }
        }

        return true;
    }

    private static void printBoard(int[][] board) {
        for(int i = 0; i < SIZE; i++) {
            if(i % 3 == 0 && i != 0) {
                System.out.println("---------------------");
            }
            for(int j = 0; j < SIZE; j++) {
                if(j % 3 == 0 && j != 0) {
                    System.out.print("| ");
                }
                System.out.print(board[i][j] == 0 ? ". " : board[i][j] + " ");
            }
            System.out.println();
        }
    }
}
