import java.util.*;
/** PuzzleSolver - Solve sliding puzzle */
public class PuzzleSolver {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] puzzle = {
            {1, 2, 3},
            {4, 0, 5},
            {6, 7, 8}
        };
        
        System.out.println("=== 8-Puzzle ===");
        printPuzzle(puzzle);
        System.out.println("Goal: 1 2 3 | 4 5 6 | 7 8 0");
        System.out.println("Use WASD to move empty space");
        
        while(true) {
            System.out.print("Move: ");
            char move = sc.next().toUpperCase().charAt(0);
            if(move == 'Q') break;
            moveTile(puzzle, move);
            printPuzzle(puzzle);
        }
        sc.close();
    }
    
    private static void printPuzzle(int[][] p) {
        for(int[] row : p) {
            for(int n : row) System.out.print(n + " ");
            System.out.println();
        }
    }
    
    private static void moveTile(int[][] p, char dir) {
        int r = 0, c = 0;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(p[i][j] == 0) { r = i; c = j; }
            }
        }
        int nr = r, nc = c;
        if(dir == 'W' && r > 0) nr--;
        else if(dir == 'S' && r < 2) nr++;
        else if(dir == 'A' && c > 0) nc--;
        else if(dir == 'D' && c < 2) nc++;
        p[r][c] = p[nr][nc];
        p[nr][nc] = 0;
    }
}
