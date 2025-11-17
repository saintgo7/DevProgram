import java.util.Scanner;

/**
 * VowelCounter - Count vowels and consonants
 * Shows breakdown of each vowel
 */
public class VowelCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Vowel Counter ===");
        System.out.print("Enter text: ");
        String text = scanner.nextLine().toLowerCase();

        int a = 0, e = 0, i = 0, o = 0, u = 0;
        int vowels = 0, consonants = 0;

        for(char c : text.toCharArray()) {
            if(Character.isLetter(c)) {
                switch(c) {
                    case 'a': a++; vowels++; break;
                    case 'e': e++; vowels++; break;
                    case 'i': i++; vowels++; break;
                    case 'o': o++; vowels++; break;
                    case 'u': u++; vowels++; break;
                    default: consonants++; break;
                }
            }
        }

        System.out.println("\n=== Results ===");
        System.out.println("Total vowels: " + vowels);
        System.out.println("  A: " + a);
        System.out.println("  E: " + e);
        System.out.println("  I: " + i);
        System.out.println("  O: " + o);
        System.out.println("  U: " + u);
        System.out.println("Consonants: " + consonants);

        scanner.close();
    }
}
