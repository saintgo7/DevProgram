import java.util.*;
/** CSVParser - Parse CSV data */
public class CSVParser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== CSV Parser ===");
        System.out.println("Enter CSV data (e.g., name,age,city):");
        String csv = sc.nextLine();
        
        String[] fields = csv.split(",");
        System.out.println("\nParsed " + fields.length + " fields:");
        for(int i = 0; i < fields.length; i++) {
            System.out.println("Field " + (i+1) + ": " + fields[i].trim());
        }
        sc.close();
    }
}
