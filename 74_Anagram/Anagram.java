import java.util.*;
/** Anagram - Check if two words are anagrams */
public class Anagram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Anagram Checker ===");
        System.out.print("Enter first word: ");
        String word1 = sc.nextLine().toLowerCase();
        System.out.print("Enter second word: ");
        String word2 = sc.nextLine().toLowerCase();
        char[] arr1 = word1.toCharArray();
        char[] arr2 = word2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        if(Arrays.equals(arr1, arr2)) {
            System.out.println("These are anagrams!");
        } else {
            System.out.println("Not anagrams.");
        }
        sc.close();
    }
}
