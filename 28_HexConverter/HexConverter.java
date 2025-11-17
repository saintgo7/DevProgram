import java.util.Scanner;

/**
 * HexConverter - Convert between decimal and hexadecimal
 * Supports both uppercase and lowercase hex
 */
public class HexConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Hexadecimal Converter ===");
        System.out.println("1. Decimal to Hex");
        System.out.println("2. Hex to Decimal");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();
        scanner.nextLine();

        if(choice == 1) {
            System.out.print("Enter decimal number: ");
            int decimal = scanner.nextInt();
            String hex = Integer.toHexString(decimal).toUpperCase();
            System.out.println("Hexadecimal: " + hex);
            System.out.println("With prefix: 0x" + hex);
        } else if(choice == 2) {
            System.out.print("Enter hex number (without 0x): ");
            String hex = scanner.nextLine();
            try {
                int decimal = Integer.parseInt(hex, 16);
                System.out.println("Decimal: " + decimal);
            } catch(NumberFormatException e) {
                System.out.println("Invalid hexadecimal number!");
            }
        } else {
            System.out.println("Invalid choice!");
        }

        scanner.close();
    }
}
