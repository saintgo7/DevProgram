import java.util.*;
/** ConnectFour - Classic connect 4 game */
public class ConnectFour {
    private static char[][] board = new char[6][7];
    private static char player = 'X';
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < 6; i++) Arrays.fill(board[i], '.');
        
        System.out.println("=== Connect Four ===");
        
        while(true) {
            printBoard();
            System.out.print("Player " + player + ", column (0-6): ");
            int col = sc.nextInt();
            
            if(!dropPiece(col)) {
                System.out.println("Column full!");
                continue;
            }
            
            if(checkWin()) {
                printBoard();
                System.out.println("Player " + player + " wins!");
                break;
            }
            
            player = player == 'X' ? 'O' : 'X';
        }
        sc.close();
    }
    
    private static void printBoard() {
        System.out.println("\n0 1 2 3 4 5 6");
        for(char[] row : board) {
            for(char c : row) System.out.print(c + " ");
            System.out.println();
        }
    }
    
    private static boolean dropPiece(int col) {
        for(int i = 5; i >= 0; i--) {
            if(board[i][col] == '.') {
                board[i][col] = player;
                return true;
            }
        }
        return false;
    }
    
    private static boolean checkWin() {
        for(int i = 0; i < 6; i++) {
            for(int j = 0; j < 7; j++) {
                if(board[i][j] == player) {
                    if(j <= 3 && board[i][j+1]==player && board[i][j+2]==player && board[i][j+3]==player) return true;
                    if(i <= 2 && board[i+1][j]==player && board[i+2][j]==player && board[i+3][j]==player) return true;
                }
            }
        }
        return false;
    }
}
