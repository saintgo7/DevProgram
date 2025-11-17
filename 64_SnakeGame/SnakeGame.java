import java.util.*;

/**
 * SnakeGame - Text-based snake game
 * Use WASD to control snake
 */
public class SnakeGame {
    private static final int WIDTH = 20;
    private static final int HEIGHT = 10;
    private static LinkedList<int[]> snake = new LinkedList<>();
    private static int[] food = new int[2];
    private static char direction = 'R';
    private static boolean gameOver = false;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        snake.add(new int[]{HEIGHT / 2, WIDTH / 2});
        placeFood();

        System.out.println("=== Snake Game ===");
        System.out.println("Controls: W(up) S(down) A(left) D(right) Q(quit)");

        while(!gameOver) {
            printBoard();
            System.out.println("Score: " + (snake.size() - 1));
            System.out.print("Move: ");

            String input = scanner.nextLine().toUpperCase();
            if(!input.isEmpty()) {
                char newDir = input.charAt(0);
                if(newDir == 'Q') break;
                if(isValidDirection(newDir)) {
                    direction = newDir;
                }
            }

            move();
        }

        System.out.println("Game Over! Final Score: " + (snake.size() - 1));
        scanner.close();
    }

    private static void printBoard() {
        char[][] board = new char[HEIGHT][WIDTH];
        for(int i = 0; i < HEIGHT; i++) {
            Arrays.fill(board[i], '.');
        }

        board[food[0]][food[1]] = 'F';

        for(int[] segment : snake) {
            if(segment[0] >= 0 && segment[0] < HEIGHT && segment[1] >= 0 && segment[1] < WIDTH) {
                board[segment[0]][segment[1]] = 'O';
            }
        }

        int[] head = snake.getFirst();
        if(head[0] >= 0 && head[0] < HEIGHT && head[1] >= 0 && head[1] < WIDTH) {
            board[head[0]][head[1]] = 'X';
        }

        System.out.println();
        for(char[] row : board) {
            System.out.println(row);
        }
    }

    private static void move() {
        int[] head = snake.getFirst();
        int[] newHead = new int[2];

        switch(direction) {
            case 'W': newHead[0] = head[0] - 1; newHead[1] = head[1]; break;
            case 'S': newHead[0] = head[0] + 1; newHead[1] = head[1]; break;
            case 'A': newHead[0] = head[0]; newHead[1] = head[1] - 1; break;
            case 'D': newHead[0] = head[0]; newHead[1] = head[1] + 1; break;
        }

        if(newHead[0] < 0 || newHead[0] >= HEIGHT || newHead[1] < 0 || newHead[1] >= WIDTH) {
            gameOver = true;
            return;
        }

        for(int[] segment : snake) {
            if(segment[0] == newHead[0] && segment[1] == newHead[1]) {
                gameOver = true;
                return;
            }
        }

        snake.addFirst(newHead);

        if(newHead[0] == food[0] && newHead[1] == food[1]) {
            placeFood();
        } else {
            snake.removeLast();
        }
    }

    private static void placeFood() {
        Random random = new Random();
        do {
            food[0] = random.nextInt(HEIGHT);
            food[1] = random.nextInt(WIDTH);
        } while(isOnSnake(food));
    }

    private static boolean isOnSnake(int[] pos) {
        for(int[] segment : snake) {
            if(segment[0] == pos[0] && segment[1] == pos[1]) return true;
        }
        return false;
    }

    private static boolean isValidDirection(char newDir) {
        if(direction == 'W' && newDir == 'S') return false;
        if(direction == 'S' && newDir == 'W') return false;
        if(direction == 'A' && newDir == 'D') return false;
        if(direction == 'D' && newDir == 'A') return false;
        return newDir == 'W' || newDir == 'S' || newDir == 'A' || newDir == 'D';
    }
}
