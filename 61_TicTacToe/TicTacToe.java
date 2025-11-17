import java.util.Scanner;

/**
 * TicTacToe - Classic 3x3 game
 * Two players take turns
 */
public class TicTacToe {
    private static char[][] board = new char[3][3];
    private static char currentPlayer = 'X';

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        initializeBoard();

        System.out.println("=== Tic Tac Toe ===");

        while(true) {
            printBoard();
            System.out.println("Player " + currentPlayer + "'s turn");
            System.out.print("Enter row (0-2): ");
            int row = scanner.nextInt();
            System.out.print("Enter column (0-2): ");
            int col = scanner.nextInt();

            if(row < 0 || row > 2 || col < 0 || col > 2) {
                System.out.println("Invalid position!");
                continue;
            }

            if(board[row][col] != '-') {
                System.out.println("Position already taken!");
                continue;
            }

            board[row][col] = currentPlayer;

            if(checkWin()) {
                printBoard();
                System.out.println("Player " + currentPlayer + " wins!");
                break;
            }

            if(isBoardFull()) {
                printBoard();
                System.out.println("It's a draw!");
                break;
            }

            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }

        scanner.close();
    }

    private static void initializeBoard() {
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }
    }

    private static void printBoard() {
        System.out.println();
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static boolean checkWin() {
        // Check rows and columns
        for(int i = 0; i < 3; i++) {
            if(board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) return true;
            if(board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer) return true;
        }

        // Check diagonals
        if(board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) return true;
        if(board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) return true;

        return false;
    }

    private static boolean isBoardFull() {
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(board[i][j] == '-') return false;
            }
        }
        return true;
    }
}
