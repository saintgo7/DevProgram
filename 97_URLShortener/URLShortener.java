import java.util.*;
/** URLShortener - Generate short URLs */
public class URLShortener {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== URL Shortener ===");
        System.out.print("Enter long URL: ");
        String longUrl = sc.nextLine();
        
        String shortCode = generateShortCode();
        String shortUrl = "https://short.url/" + shortCode;
        
        System.out.println("\n--- Shortened URL ---");
        System.out.println("Original: " + longUrl);
        System.out.println("Shortened: " + shortUrl);
        System.out.println("Short code: " + shortCode);
        sc.close();
    }
    
    private static String generateShortCode() {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder code = new StringBuilder();
        Random rand = new Random();
        for(int i = 0; i < 6; i++) {
            code.append(chars.charAt(rand.nextInt(chars.length())));
        }
        return code.toString();
    }
}
