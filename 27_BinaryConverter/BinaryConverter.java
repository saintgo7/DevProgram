import java.util.Scanner;

/**
 * BinaryConverter - Convert decimal to binary and vice versa
 * Also shows conversion steps
 */
public class BinaryConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Binary Converter ===");
        System.out.println("1. Decimal to Binary");
        System.out.println("2. Binary to Decimal");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();
        scanner.nextLine();

        if(choice == 1) {
            System.out.print("Enter decimal number: ");
            int decimal = scanner.nextInt();
            String binary = Integer.toBinaryString(decimal);
            System.out.println("Binary: " + binary);
        } else if(choice == 2) {
            System.out.print("Enter binary number: ");
            String binary = scanner.nextLine();
            try {
                int decimal = Integer.parseInt(binary, 2);
                System.out.println("Decimal: " + decimal);
            } catch(NumberFormatException e) {
                System.out.println("Invalid binary number!");
            }
        } else {
            System.out.println("Invalid choice!");
        }

        scanner.close();
    }
}
