import java.util.ArrayList;
import java.util.Scanner;

/**
 * ArrayList - ArrayList demonstration
 * Dynamic array with random access
 */
public class ArrayListDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== ArrayList Operations ===");
            System.out.println("1. Add element");
            System.out.println("2. Remove element");
            System.out.println("3. Search element");
            System.out.println("4. Get by index");
            System.out.println("5. Display all");
            System.out.println("6. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch(choice) {
                case 1:
                    System.out.print("Enter element: ");
                    String element = scanner.nextLine();
                    list.add(element);
                    System.out.println("Added!");
                    break;
                case 2:
                    System.out.print("Enter element to remove: ");
                    String toRemove = scanner.nextLine();
                    if(list.remove(toRemove)) {
                        System.out.println("Removed!");
                    } else {
                        System.out.println("Element not found!");
                    }
                    break;
                case 3:
                    System.out.print("Enter element to search: ");
                    String search = scanner.nextLine();
                    int index = list.indexOf(search);
                    if(index != -1) {
                        System.out.println("Found at index: " + index);
                    } else {
                        System.out.println("Not found!");
                    }
                    break;
                case 4:
                    System.out.print("Enter index: ");
                    int idx = scanner.nextInt();
                    if(idx >= 0 && idx < list.size()) {
                        System.out.println("Element: " + list.get(idx));
                    } else {
                        System.out.println("Invalid index!");
                    }
                    break;
                case 5:
                    System.out.println("ArrayList: " + list);
                    System.out.println("Size: " + list.size());
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
