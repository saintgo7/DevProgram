import java.util.*;
/** ChessValidator - Validate chess moves */
public class ChessValidator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Chess Move Validator ===");
        System.out.print("Piece (K/Q/R/B/N/P): ");
        char piece = sc.next().toUpperCase().charAt(0);
        System.out.print("From (e.g., e2): ");
        String from = sc.next();
        System.out.print("To (e.g., e4): ");
        String to = sc.next();
        
        boolean valid = validateMove(piece, from, to);
        System.out.println(valid ? "Valid move!" : "Invalid move!");
        sc.close();
    }
    
    private static boolean validateMove(char piece, String from, String to) {
        int fx = from.charAt(0) - 'a', fy = from.charAt(1) - '1';
        int tx = to.charAt(0) - 'a', ty = to.charAt(1) - '1';
        int dx = Math.abs(tx - fx), dy = Math.abs(ty - fy);
        
        switch(piece) {
            case 'K': return dx <= 1 && dy <= 1;
            case 'Q': return dx == dy || fx == tx || fy == ty;
            case 'R': return fx == tx || fy == ty;
            case 'B': return dx == dy;
            case 'N': return (dx == 2 && dy == 1) || (dx == 1 && dy == 2);
            case 'P': return fx == tx && dy == 1;
            default: return false;
        }
    }
}
