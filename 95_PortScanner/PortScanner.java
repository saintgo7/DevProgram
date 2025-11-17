import java.util.*;
/** PortScanner - Common port checker */
public class PortScanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Port Scanner (Educational) ===");
        System.out.print("Enter host: ");
        String host = sc.nextLine();
        
        int[] commonPorts = {21, 22, 23, 25, 80, 443, 3306, 8080};
        String[] services = {"FTP", "SSH", "Telnet", "SMTP", "HTTP", "HTTPS", "MySQL", "HTTP-Alt"};
        
        System.out.println("\nScanning common ports on " + host + "...");
        for(int i = 0; i < commonPorts.length; i++) {
            System.out.println("Port " + commonPorts[i] + " (" + services[i] + "): " + 
                             (Math.random() > 0.7 ? "OPEN" : "CLOSED"));
        }
        sc.close();
    }
}
