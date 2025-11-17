import java.util.*;
/** Boggle - Find words in letter grid */
public class Boggle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[][] board = {
            {'A','B','C','D'},
            {'E','F','G','H'},
            {'I','J','K','L'},
            {'M','N','O','P'}
        };
        System.out.println("=== Boggle ===");
        for(char[] row : board) {
            for(char c : row) System.out.print(c + " ");
            System.out.println();
        }
        System.out.println("\nEnter words you find (type 'done' to finish):");
        Set<String> words = new HashSet<>();
        while(true) {
            String word = sc.nextLine().toUpperCase();
            if(word.equals("DONE")) break;
            words.add(word);
        }
        System.out.println("You found " + words.size() + " words!");
        sc.close();
    }
}
