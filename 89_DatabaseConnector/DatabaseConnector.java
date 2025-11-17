import java.util.*;
/** DatabaseConnector - Database connection simulator */
public class DatabaseConnector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Database Connector (Simulator) ===");
        System.out.print("Host: ");
        String host = sc.nextLine();
        System.out.print("Database: ");
        String db = sc.nextLine();
        System.out.print("Username: ");
        String user = sc.nextLine();
        
        System.out.println("\nConnecting to " + db + " on " + host + "...");
        System.out.println("Connection successful!");
        System.out.println("Connection string: jdbc:mysql://" + host + "/" + db);
        sc.close();
    }
}
