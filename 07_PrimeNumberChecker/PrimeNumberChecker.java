import java.util.Scanner;

/**
 * PrimeNumberChecker - Check if a number is prime
 * Also lists all prime numbers up to a given number
 */
public class PrimeNumberChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Prime Number Checker ===");
        System.out.println("1. Check if number is prime");
        System.out.println("2. List all primes up to N");
        System.out.print("Choose option: ");

        int choice = scanner.nextInt();

        if(choice == 1) {
            System.out.print("Enter number: ");
            int num = scanner.nextInt();
            if(isPrime(num)) {
                System.out.println(num + " is a prime number");
            } else {
                System.out.println(num + " is not a prime number");
            }
        } else if(choice == 2) {
            System.out.print("Enter upper limit: ");
            int limit = scanner.nextInt();
            System.out.println("Prime numbers up to " + limit + ":");
            for(int i = 2; i <= limit; i++) {
                if(isPrime(i)) {
                    System.out.print(i + " ");
                }
            }
            System.out.println();
        }

        scanner.close();
    }

    private static boolean isPrime(int n) {
        if(n <= 1) return false;
        if(n <= 3) return true;
        if(n % 2 == 0 || n % 3 == 0) return false;
        for(int i = 5; i * i <= n; i += 6) {
            if(n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
}
