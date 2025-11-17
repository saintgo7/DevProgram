import java.util.Scanner;
import java.math.BigInteger;

/**
 * FactorialCalculator - Calculate factorial of a number
 * Supports large numbers using BigInteger
 */
public class FactorialCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Factorial Calculator ===");
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();

        if(n < 0) {
            System.out.println("Factorial is not defined for negative numbers!");
        } else {
            BigInteger result = factorial(n);
            System.out.println(n + "! = " + result);
        }

        scanner.close();
    }

    private static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for(int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }
}
