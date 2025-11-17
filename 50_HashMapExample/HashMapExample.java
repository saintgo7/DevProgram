import java.util.HashMap;
import java.util.Scanner;

/**
 * HashMapExample - HashMap demonstration
 * Key-value pair storage with O(1) access
 */
public class HashMapExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, String> map = new HashMap<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== HashMap Operations ===");
            System.out.println("1. Put (Add)");
            System.out.println("2. Get (Retrieve)");
            System.out.println("3. Remove");
            System.out.println("4. Check key exists");
            System.out.println("5. Display all");
            System.out.println("6. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch(choice) {
                case 1:
                    System.out.print("Enter key: ");
                    String key = scanner.nextLine();
                    System.out.print("Enter value: ");
                    String value = scanner.nextLine();
                    map.put(key, value);
                    System.out.println("Added!");
                    break;
                case 2:
                    System.out.print("Enter key: ");
                    String getKey = scanner.nextLine();
                    String result = map.get(getKey);
                    if(result != null) {
                        System.out.println("Value: " + result);
                    } else {
                        System.out.println("Key not found!");
                    }
                    break;
                case 3:
                    System.out.print("Enter key to remove: ");
                    String removeKey = scanner.nextLine();
                    if(map.remove(removeKey) != null) {
                        System.out.println("Removed!");
                    } else {
                        System.out.println("Key not found!");
                    }
                    break;
                case 4:
                    System.out.print("Enter key to check: ");
                    String checkKey = scanner.nextLine();
                    if(map.containsKey(checkKey)) {
                        System.out.println("Key exists!");
                    } else {
                        System.out.println("Key does not exist!");
                    }
                    break;
                case 5:
                    System.out.println("HashMap contents:");
                    map.forEach((k, v) -> System.out.println(k + " => " + v));
                    System.out.println("Size: " + map.size());
                    break;
                case 6:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        }

        scanner.close();
    }
}
