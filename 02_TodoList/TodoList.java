import java.util.ArrayList;
import java.util.Scanner;

/**
 * TodoList - Simple task management system
 * Add, view, complete, and delete tasks
 */
public class TodoList {
    private static ArrayList<String> tasks = new ArrayList<>();
    private static ArrayList<Boolean> completed = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while(running) {
            System.out.println("\n=== Todo List ===");
            System.out.println("1. Add task");
            System.out.println("2. View tasks");
            System.out.println("3. Complete task");
            System.out.println("4. Delete task");
            System.out.println("5. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch(choice) {
                case 1:
                    System.out.print("Enter task: ");
                    String task = scanner.nextLine();
                    tasks.add(task);
                    completed.add(false);
                    System.out.println("Task added!");
                    break;
                case 2:
                    viewTasks();
                    break;
                case 3:
                    System.out.print("Enter task number to complete: ");
                    int completeIdx = scanner.nextInt() - 1;
                    if(completeIdx >= 0 && completeIdx < tasks.size()) {
                        completed.set(completeIdx, true);
                        System.out.println("Task completed!");
                    } else {
                        System.out.println("Invalid task number!");
                    }
                    break;
                case 4:
                    System.out.print("Enter task number to delete: ");
                    int deleteIdx = scanner.nextInt() - 1;
                    if(deleteIdx >= 0 && deleteIdx < tasks.size()) {
                        tasks.remove(deleteIdx);
                        completed.remove(deleteIdx);
                        System.out.println("Task deleted!");
                    } else {
                        System.out.println("Invalid task number!");
                    }
                    break;
                case 5:
                    running = false;
                    System.out.println("Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option!");
            }
        }
        scanner.close();
    }

    private static void viewTasks() {
        if(tasks.isEmpty()) {
            System.out.println("No tasks!");
            return;
        }
        System.out.println("\nYour tasks:");
        for(int i = 0; i < tasks.size(); i++) {
            String status = completed.get(i) ? "[✓]" : "[ ]";
            System.out.println((i + 1) + ". " + status + " " + tasks.get(i));
        }
    }
}
