import java.util.*;
/** QRCodeGenerator - QR code text generator */
public class QRCodeGenerator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== QR Code Generator (Text) ===");
        System.out.print("Enter text to encode: ");
        String text = sc.nextLine();
        
        System.out.println("\n--- QR Code (Simplified) ---");
        int size = 10;
        Random rand = new Random(text.hashCode());
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                System.out.print(rand.nextBoolean() ? "██" : "  ");
            }
            System.out.println();
        }
        System.out.println("\nEncoded text: " + text);
        sc.close();
    }
}
