import java.util.*;
/** BingoGame - Simple bingo number caller */
public class BingoGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        for(int i = 1; i <= 75; i++) numbers.add(i);
        Collections.shuffle(numbers);
        System.out.println("=== Bingo Caller ===");
        int called = 0;
        while(called < numbers.size()) {
            System.out.print("Press Enter to call next number...");
            sc.nextLine();
            int num = numbers.get(called++);
            char letter = num <= 15 ? 'B' : num <= 30 ? 'I' : 
                         num <= 45 ? 'N' : num <= 60 ? 'G' : 'O';
            System.out.println(letter + "-" + num);
            System.out.println("Called: " + called + "/75");
        }
        sc.close();
    }
}
