import java.util.*;
/** JSONParser - Simple JSON key-value extractor */
public class JSONParser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Simple JSON Parser ===");
        System.out.println("Enter JSON (e.g., {\"name\":\"John\",\"age\":30}):");
        String json = sc.nextLine();
        
        json = json.replaceAll("[{}]", "");
        String[] pairs = json.split(",");
        
        System.out.println("\nExtracted key-value pairs:");
        for(String pair : pairs) {
            String[] kv = pair.split(":");
            if(kv.length == 2) {
                String key = kv[0].trim().replaceAll("\"", "");
                String value = kv[1].trim().replaceAll("\"", "");
                System.out.println(key + " = " + value);
            }
        }
        sc.close();
    }
}
