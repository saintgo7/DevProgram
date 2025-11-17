import java.util.*;
/** MazeGenerator - Generate random maze */
public class MazeGenerator {
    public static void main(String[] args) {
        int size = 10;
        char[][] maze = new char[size][size];
        Random rand = new Random();
        
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                maze[i][j] = rand.nextBoolean() ? '#' : ' ';
            }
        }
        
        maze[0][0] = 'S';
        maze[size-1][size-1] = 'E';
        
        System.out.println("=== Generated Maze ===");
        for(char[] row : maze) {
            for(char c : row) System.out.print(c + " ");
            System.out.println();
        }
    }
}
