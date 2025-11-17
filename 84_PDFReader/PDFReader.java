import java.util.*;
/** PDFReader - PDF metadata simulator */
public class PDFReader {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== PDF Info Reader (Simulator) ===");
        System.out.print("Enter PDF filename: ");
        String filename = sc.nextLine();
        System.out.println("\n--- PDF Information ---");
        System.out.println("Filename: " + filename);
        System.out.println("Pages: " + (int)(Math.random()*100 + 1));
        System.out.println("Size: " + (int)(Math.random()*10 + 1) + " MB");
        System.out.println("Created: 2024-01-01");
        sc.close();
    }
}
