import java.util.*;
/** BarcodeGenerator - ASCII barcode generator */
public class BarcodeGenerator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Barcode Generator (ASCII) ===");
        System.out.print("Enter number to encode: ");
        String number = sc.nextLine();
        
        System.out.println("\n--- Barcode ---");
        for(int i = 0; i < 3; i++) {
            for(char c : number.toCharArray()) {
                int digit = c - '0';
                System.out.print(digit % 2 == 0 ? "█  " : " ██ ");
            }
            System.out.println();
        }
        System.out.println(number);
        sc.close();
    }
}
