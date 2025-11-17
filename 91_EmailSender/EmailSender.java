import java.util.*;
/** EmailSender - Email composition tool */
public class EmailSender {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Email Composer ===");
        System.out.print("To: ");
        String to = sc.nextLine();
        System.out.print("Subject: ");
        String subject = sc.nextLine();
        System.out.print("Body: ");
        String body = sc.nextLine();
        
        System.out.println("\n--- Email Preview ---");
        System.out.println("To: " + to);
        System.out.println("Subject: " + subject);
        System.out.println("Body: " + body);
        System.out.println("\n[Email would be sent here]");
        sc.close();
    }
}
