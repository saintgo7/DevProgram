import java.util.*;
/** WordScramble - Unscramble the word */
public class WordScramble {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] words = {"java", "programming", "computer", "algorithm", "developer"};
        Random rand = new Random();
        int score = 0;
        System.out.println("=== Word Scramble ===");
        for(int i = 0; i < 5; i++) {
            String word = words[rand.nextInt(words.length)];
            String scrambled = scramble(word);
            System.out.print("\nUnscramble: " + scrambled + " -> ");
            String guess = sc.nextLine().toLowerCase();
            if(guess.equals(word)) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong! It was: " + word);
            }
        }
        System.out.println("\nScore: " + score + "/5");
        sc.close();
    }
    private static String scramble(String word) {
        List<Character> chars = new ArrayList<>();
        for(char c : word.toCharArray()) chars.add(c);
        Collections.shuffle(chars);
        StringBuilder sb = new StringBuilder();
        for(char c : chars) sb.append(c);
        return sb.toString();
    }
}
