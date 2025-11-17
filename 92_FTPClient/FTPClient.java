import java.util.*;
/** FTPClient - FTP connection simulator */
public class FTPClient {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== FTP Client (Simulator) ===");
        System.out.print("FTP Server: ");
        String server = sc.nextLine();
        System.out.print("Username: ");
        String user = sc.nextLine();
        
        System.out.println("\nConnecting to " + server + "...");
        System.out.println("Connected as " + user);
        System.out.println("Remote directory: /home/" + user);
        System.out.println("Type 'ls' to list files, 'quit' to exit");
        
        while(true) {
            System.out.print("ftp> ");
            String cmd = sc.nextLine();
            if(cmd.equals("quit")) break;
            if(cmd.equals("ls")) {
                System.out.println("file1.txt\nfile2.txt\ndocuments/");
            }
        }
        sc.close();
    }
}
