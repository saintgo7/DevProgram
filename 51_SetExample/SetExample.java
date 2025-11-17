import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * SetExample - HashSet demonstration
 * Collection with unique elements only
 */
public class SetExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Set<String> set = new HashSet<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== Set Operations ===");
            System.out.println("1. Add element");
            System.out.println("2. Remove element");
            System.out.println("3. Check contains");
            System.out.println("4. Display all");
            System.out.println("5. Clear set");
            System.out.println("6. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch(choice) {
                case 1:
                    System.out.print("Enter element: ");
                    String element = scanner.nextLine();
                    if(set.add(element)) {
                        System.out.println("Added!");
                    } else {
                        System.out.println("Element already exists!");
                    }
                    break;
                case 2:
                    System.out.print("Enter element to remove: ");
                    String remove = scanner.nextLine();
                    if(set.remove(remove)) {
                        System.out.println("Removed!");
                    } else {
                        System.out.println("Element not found!");
                    }
                    break;
                case 3:
                    System.out.print("Enter element to check: ");
                    String check = scanner.nextLine();
                    if(set.contains(check)) {
                        System.out.println("Element exists!");
                    } else {
                        System.out.println("Element does not exist!");
                    }
                    break;
                case 4:
                    System.out.println("Set: " + set);
                    System.out.println("Size: " + set.size());
                    break;
                case 5:
                    set.clear();
                    System.out.println("Set cleared!");
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
