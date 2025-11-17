import java.util.LinkedList;
import java.util.Scanner;

/**
 * LinkedList - Linked list data structure demonstration
 * Dynamic list with efficient insertions/deletions
 */
public class LinkedListDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== Linked List Operations ===");
            System.out.println("1. Add at end");
            System.out.println("2. Add at beginning");
            System.out.println("3. Remove first");
            System.out.println("4. Remove last");
            System.out.println("5. Display");
            System.out.println("6. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();

            switch(choice) {
                case 1:
                    System.out.print("Enter value: ");
                    list.addLast(scanner.nextInt());
                    break;
                case 2:
                    System.out.print("Enter value: ");
                    list.addFirst(scanner.nextInt());
                    break;
                case 3:
                    if(!list.isEmpty()) {
                        System.out.println("Removed: " + list.removeFirst());
                    } else {
                        System.out.println("List is empty!");
                    }
                    break;
                case 4:
                    if(!list.isEmpty()) {
                        System.out.println("Removed: " + list.removeLast());
                    } else {
                        System.out.println("List is empty!");
                    }
                    break;
                case 5:
                    System.out.println("List: " + list);
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
