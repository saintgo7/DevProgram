import java.util.*;
/** IPValidator - Validate IP addresses */
public class IPValidator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== IP Address Validator ===");
        System.out.print("Enter IP address: ");
        String ip = sc.nextLine();
        
        if(isValidIPv4(ip)) {
            System.out.println("Valid IPv4 address!");
            String[] parts = ip.split("\\.");
            System.out.println("Class: " + getIPClass(Integer.parseInt(parts[0])));
        } else {
            System.out.println("Invalid IP address!");
        }
        sc.close();
    }
    
    private static boolean isValidIPv4(String ip) {
        String[] parts = ip.split("\\.");
        if(parts.length != 4) return false;
        for(String part : parts) {
            try {
                int num = Integer.parseInt(part);
                if(num < 0 || num > 255) return false;
            } catch(NumberFormatException e) {
                return false;
            }
        }
        return true;
    }
    
    private static String getIPClass(int first) {
        if(first < 128) return "A";
        if(first < 192) return "B";
        if(first < 224) return "C";
        if(first < 240) return "D";
        return "E";
    }
}
