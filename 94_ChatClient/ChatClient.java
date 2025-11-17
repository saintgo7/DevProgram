import java.util.*;
/** ChatClient - Chat client simulator */
public class ChatClient {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Chat Client ===");
        System.out.print("Server address: ");
        String server = sc.nextLine();
        System.out.print("Username: ");
        String username = sc.nextLine();
        
        System.out.println("Connecting to " + server + "...");
        System.out.println("Connected! Type messages:");
        
        while(true) {
            System.out.print("> ");
            String msg = sc.nextLine();
            if(msg.equals("/quit")) break;
            System.out.println("[You]: " + msg);
        }
        sc.close();
    }
}
