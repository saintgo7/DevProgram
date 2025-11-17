import java.util.*;
/** MathQuiz - Random math problems */
public class MathQuiz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        int score = 0;
        System.out.println("=== Math Quiz ===");
        for(int i = 1; i <= 10; i++) {
            int a = rand.nextInt(20) + 1;
            int b = rand.nextInt(20) + 1;
            int op = rand.nextInt(4);
            int answer = 0;
            String opStr = "";
            switch(op) {
                case 0: answer = a + b; opStr = "+"; break;
                case 1: answer = a - b; opStr = "-"; break;
                case 2: answer = a * b; opStr = "*"; break;
                case 3: answer = a / b; opStr = "/"; b = b == 0 ? 1 : b; break;
            }
            System.out.print("Q" + i + ": " + a + " " + opStr + " " + b + " = ");
            int userAns = sc.nextInt();
            if(userAns == answer) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong! Answer was " + answer);
            }
        }
        System.out.println("\nScore: " + score + "/10");
        sc.close();
    }
}
