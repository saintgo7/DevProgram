import java.util.Scanner;
import java.util.Stack;

/**
 * Stack - Stack data structure demonstration
 * LIFO (Last In First Out) operations
 */
public class StackDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();

        boolean running = true;

        while(running) {
            System.out.println("\n=== Stack Operations ===");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();

            switch(choice) {
                case 1:
                    System.out.print("Enter value to push: ");
                    int value = scanner.nextInt();
                    stack.push(value);
                    System.out.println("Pushed: " + value);
                    break;
                case 2:
                    if(!stack.isEmpty()) {
                        System.out.println("Popped: " + stack.pop());
                    } else {
                        System.out.println("Stack is empty!");
                    }
                    break;
                case 3:
                    if(!stack.isEmpty()) {
                        System.out.println("Top: " + stack.peek());
                    } else {
                        System.out.println("Stack is empty!");
                    }
                    break;
                case 4:
                    System.out.println("Stack: " + stack);
                    System.out.println("Size: " + stack.size());
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
