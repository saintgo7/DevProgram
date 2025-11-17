import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * FileReader - Read and display file contents
 * Supports line-by-line reading with line numbers
 */
public class FileReader {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== File Reader ===");
        System.out.print("Enter file path: ");
        String filePath = scanner.nextLine();

        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(new FileInputStream(filePath)))) {

            String line;
            int lineNumber = 1;

            System.out.println("\n--- File Contents ---");
            while((line = br.readLine()) != null) {
                System.out.printf("%4d: %s%n", lineNumber++, line);
            }
            System.out.println("--- End of File ---");
            System.out.println("Total lines: " + (lineNumber - 1));

        } catch(Exception e) {
            System.out.println("Error reading file: " + e.getMessage());
        }

        scanner.close();
    }
}
