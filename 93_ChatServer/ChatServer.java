import java.util.*;
/** ChatServer - Simple chat room simulator */
public class ChatServer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Chat Server ===");
        System.out.print("Enter your username: ");
        String username = sc.nextLine();
        
        System.out.println("Connected to chat server!");
        System.out.println("Type messages (or 'quit' to exit):");
        
        while(true) {
            System.out.print(username + ": ");
            String msg = sc.nextLine();
            if(msg.equals("quit")) break;
            System.out.println("[" + new Date() + "] " + username + ": " + msg);
        }
        sc.close();
    }
}
