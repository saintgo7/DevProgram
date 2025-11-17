import java.util.*;
/** LogAnalyzer - Analyze log file patterns */
public class LogAnalyzer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Log Analyzer ===");
        System.out.println("Enter log entries (type 'END' to finish):");
        
        Map<String, Integer> levels = new HashMap<>();
        int total = 0;
        
        while(true) {
            String line = sc.nextLine();
            if(line.equals("END")) break;
            total++;
            
            if(line.contains("ERROR")) levels.put("ERROR", levels.getOrDefault("ERROR", 0) + 1);
            else if(line.contains("WARN")) levels.put("WARN", levels.getOrDefault("WARN", 0) + 1);
            else if(line.contains("INFO")) levels.put("INFO", levels.getOrDefault("INFO", 0) + 1);
        }
        
        System.out.println("\n--- Log Summary ---");
        System.out.println("Total entries: " + total);
        levels.forEach((k,v) -> System.out.println(k + ": " + v));
        sc.close();
    }
}
