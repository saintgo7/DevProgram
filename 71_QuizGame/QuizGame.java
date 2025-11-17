import java.util.*;
/** QuizGame - Multiple choice quiz */
public class QuizGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[][] questions = {
            {"What is 2+2?", "3", "4", "5", "2"},
            {"Capital of France?", "London", "Paris", "Berlin", "2"},
            {"Largest planet?", "Earth", "Mars", "Jupiter", "3"}
        };
        int score = 0;
        System.out.println("=== Quiz Game ===");
        for(int i = 0; i < questions.length; i++) {
            System.out.println("\nQ" + (i+1) + ": " + questions[i][0]);
            System.out.println("1. " + questions[i][1]);
            System.out.println("2. " + questions[i][2]);
            System.out.println("3. " + questions[i][3]);
            System.out.print("Answer: ");
            int ans = sc.nextInt();
            if(ans == Integer.parseInt(questions[i][4])) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong!");
            }
        }
        System.out.println("\nFinal Score: " + score + "/" + questions.length);
        sc.close();
    }
}
