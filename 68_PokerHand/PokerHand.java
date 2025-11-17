import java.util.*;
/**
 * PokerHand - Evaluate poker hand rankings
 */
public class PokerHand {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Poker Hand Evaluator ===");
        System.out.println("Enter 5 cards (e.g., AS KH QD JC 10S):");
        String[] cards = sc.nextLine().split(" ");
        System.out.println("Hand: " + evaluateHand(cards));
        sc.close();
    }
    private static String evaluateHand(String[] cards) {
        if(cards.length != 5) return "Invalid hand";
        int[] values = new int[5];
        char[] suits = new char[5];
        for(int i = 0; i < 5; i++) {
            suits[i] = cards[i].charAt(cards[i].length()-1);
            String val = cards[i].substring(0, cards[i].length()-1);
            values[i] = val.equals("A") ? 14 : val.equals("K") ? 13 :
                       val.equals("Q") ? 12 : val.equals("J") ? 11 : Integer.parseInt(val);
        }
        Arrays.sort(values);
        boolean flush = true;
        for(int i = 1; i < 5; i++) if(suits[i] != suits[0]) flush = false;
        boolean straight = true;
        for(int i = 1; i < 5; i++) if(values[i] != values[i-1] + 1) straight = false;
        if(flush && straight) return "Straight Flush";
        if(flush) return "Flush";
        if(straight) return "Straight";
        Map<Integer,Integer> freq = new HashMap<>();
        for(int v : values) freq.put(v, freq.getOrDefault(v,0)+1);
        if(freq.containsValue(4)) return "Four of a Kind";
        if(freq.containsValue(3) && freq.containsValue(2)) return "Full House";
        if(freq.containsValue(3)) return "Three of a Kind";
        int pairs = 0;
        for(int f : freq.values()) if(f == 2) pairs++;
        if(pairs == 2) return "Two Pair";
        if(pairs == 1) return "One Pair";
        return "High Card";
    }
}
