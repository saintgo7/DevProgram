import java.util.*;
/** Crossword - Simple crossword puzzle */
public class Crossword {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Crossword Puzzle ===");
        System.out.println("1. Programming language (4 letters): J _ _ _");
        System.out.println("2. Data structure (5 letters): _ R R _ _");
        System.out.println("3. Loop type (3 letters): F _ _");
        
        String[] answers = {"JAVA", "ARRAY", "FOR"};
        int score = 0;
        
        for(int i = 0; i < answers.length; i++) {
            System.out.print("Answer " + (i+1) + ": ");
            String ans = sc.nextLine().toUpperCase();
            if(ans.equals(answers[i])) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong! Answer: " + answers[i]);
            }
        }
        System.out.println("\nScore: " + score + "/3");
        sc.close();
    }
}
