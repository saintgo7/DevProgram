import java.util.*;
/** WebScraper - URL parser and analyzer */
public class WebScraper {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Web Scraper (URL Analyzer) ===");
        System.out.print("Enter URL: ");
        String url = sc.nextLine();
        
        System.out.println("\n--- URL Analysis ---");
        String[] parts = url.split("://");
        if(parts.length > 1) {
            System.out.println("Protocol: " + parts[0]);
            String[] domainPath = parts[1].split("/", 2);
            System.out.println("Domain: " + domainPath[0]);
            if(domainPath.length > 1) {
                System.out.println("Path: /" + domainPath[1]);
            }
        }
        sc.close();
    }
}
