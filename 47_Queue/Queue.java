import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * Queue - Queue data structure demonstration
 * FIFO (First In First Out) operations
 */
public class QueueDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== Queue Operations ===");
            System.out.println("1. Enqueue (Add)");
            System.out.println("2. Dequeue (Remove)");
            System.out.println("3. Peek (Front)");
            System.out.println("4. Display");
            System.out.println("5. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();

            switch(choice) {
                case 1:
                    System.out.print("Enter value: ");
                    int value = scanner.nextInt();
                    queue.offer(value);
                    System.out.println("Enqueued: " + value);
                    break;
                case 2:
                    if(!queue.isEmpty()) {
                        System.out.println("Dequeued: " + queue.poll());
                    } else {
                        System.out.println("Queue is empty!");
                    }
                    break;
                case 3:
                    if(!queue.isEmpty()) {
                        System.out.println("Front: " + queue.peek());
                    } else {
                        System.out.println("Queue is empty!");
                    }
                    break;
                case 4:
                    System.out.println("Queue: " + queue);
                    System.out.println("Size: " + queue.size());
                    break;
                case 5:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        }

        scanner.close();
    }
}
