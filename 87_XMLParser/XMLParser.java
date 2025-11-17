import java.util.*;
/** XMLParser - Simple XML tag extractor */
public class XMLParser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Simple XML Parser ===");
        System.out.println("Enter XML (e.g., <name>John</name>):");
        String xml = sc.nextLine();
        
        int start = xml.indexOf('>');
        int end = xml.indexOf('<', 1);
        
        if(start != -1 && end != -1) {
            String tagName = xml.substring(1, start);
            String content = xml.substring(start + 1, end);
            System.out.println("Tag: " + tagName);
            System.out.println("Content: " + content);
        } else {
            System.out.println("Invalid XML format");
        }
        sc.close();
    }
}
