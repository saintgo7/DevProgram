import java.util.Scanner;
import java.util.TreeSet;

/**
 * TreeExample - TreeSet demonstration
 * Sorted set with natural ordering
 */
public class TreeExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TreeSet<Integer> tree = new TreeSet<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== TreeSet Operations ===");
            System.out.println("1. Add element");
            System.out.println("2. Remove element");
            System.out.println("3. Get first");
            System.out.println("4. Get last");
            System.out.println("5. Display (sorted)");
            System.out.println("6. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();

            switch(choice) {
                case 1:
                    System.out.print("Enter number: ");
                    int num = scanner.nextInt();
                    if(tree.add(num)) {
                        System.out.println("Added!");
                    } else {
                        System.out.println("Number already exists!");
                    }
                    break;
                case 2:
                    System.out.print("Enter number to remove: ");
                    int remove = scanner.nextInt();
                    if(tree.remove(remove)) {
                        System.out.println("Removed!");
                    } else {
                        System.out.println("Number not found!");
                    }
                    break;
                case 3:
                    if(!tree.isEmpty()) {
                        System.out.println("First (smallest): " + tree.first());
                    } else {
                        System.out.println("Tree is empty!");
                    }
                    break;
                case 4:
                    if(!tree.isEmpty()) {
                        System.out.println("Last (largest): " + tree.last());
                    } else {
                        System.out.println("Tree is empty!");
                    }
                    break;
                case 5:
                    System.out.println("TreeSet (sorted): " + tree);
                    System.out.println("Size: " + tree.size());
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
