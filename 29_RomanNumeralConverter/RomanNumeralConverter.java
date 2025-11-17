import java.util.Scanner;

/**
 * RomanNumeralConverter - Convert between decimal and Roman numerals
 * Supports numbers 1-3999
 */
public class RomanNumeralConverter {
    private static final int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Roman Numeral Converter ===");
        System.out.println("1. Decimal to Roman");
        System.out.println("2. Roman to Decimal");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();
        scanner.nextLine();

        if(choice == 1) {
            System.out.print("Enter decimal number (1-3999): ");
            int num = scanner.nextInt();
            if(num < 1 || num > 3999) {
                System.out.println("Number must be between 1 and 3999!");
            } else {
                System.out.println("Roman numeral: " + toRoman(num));
            }
        } else if(choice == 2) {
            System.out.print("Enter Roman numeral: ");
            String roman = scanner.nextLine().toUpperCase();
            System.out.println("Decimal: " + toDecimal(roman));
        }

        scanner.close();
    }

    private static String toRoman(int num) {
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < values.length && num > 0; i++) {
            while(num >= values[i]) {
                num -= values[i];
                result.append(symbols[i]);
            }
        }
        return result.toString();
    }

    private static int toDecimal(String roman) {
        int result = 0;
        int prevValue = 0;
        for(int i = roman.length() - 1; i >= 0; i--) {
            int value = getValue(roman.charAt(i));
            if(value < prevValue) {
                result -= value;
            } else {
                result += value;
            }
            prevValue = value;
        }
        return result;
    }

    private static int getValue(char c) {
        switch(c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}
