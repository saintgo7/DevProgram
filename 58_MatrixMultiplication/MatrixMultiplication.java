import java.util.Scanner;

/**
 * MatrixMultiplication - Multiply two matrices
 * Validates dimensions and performs multiplication
 */
public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Matrix Multiplication ===");

        System.out.print("Enter rows of first matrix: ");
        int r1 = scanner.nextInt();
        System.out.print("Enter columns of first matrix: ");
        int c1 = scanner.nextInt();

        int[][] matrix1 = new int[r1][c1];
        System.out.println("Enter first matrix:");
        for(int i = 0; i < r1; i++) {
            for(int j = 0; j < c1; j++) {
                matrix1[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Enter rows of second matrix: ");
        int r2 = scanner.nextInt();
        System.out.print("Enter columns of second matrix: ");
        int c2 = scanner.nextInt();

        if(c1 != r2) {
            System.out.println("Cannot multiply! Columns of first must equal rows of second.");
            scanner.close();
            return;
        }

        int[][] matrix2 = new int[r2][c2];
        System.out.println("Enter second matrix:");
        for(int i = 0; i < r2; i++) {
            for(int j = 0; j < c2; j++) {
                matrix2[i][j] = scanner.nextInt();
            }
        }

        int[][] result = multiply(matrix1, matrix2);

        System.out.println("\nResult:");
        printMatrix(result);

        scanner.close();
    }

    private static int[][] multiply(int[][] a, int[][] b) {
        int rows = a.length;
        int cols = b[0].length;
        int common = b.length;

        int[][] result = new int[rows][cols];

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                for(int k = 0; k < common; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        return result;
    }

    private static void printMatrix(int[][] matrix) {
        for(int[] row : matrix) {
            for(int val : row) {
                System.out.print(val + "\t");
            }
            System.out.println();
        }
    }
}
