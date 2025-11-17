import java.util.*;
/** Lottery - Random number lottery generator */
public class Lottery {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Lottery Number Generator ===");
        System.out.print("How many numbers to pick? ");
        int count = sc.nextInt();
        System.out.print("From range 1 to? ");
        int max = sc.nextInt();
        Set<Integer> numbers = new TreeSet<>();
        Random rand = new Random();
        while(numbers.size() < count) {
            numbers.add(rand.nextInt(max) + 1);
        }
        System.out.println("Your lucky numbers: " + numbers);
        sc.close();
    }
}
