import java.util.*;

/**
 * GraphExample - Simple graph data structure
 * Adjacency list representation
 */
public class GraphExample {
    private Map<Integer, List<Integer>> adjacencyList;

    public GraphExample() {
        adjacencyList = new HashMap<>();
    }

    public void addVertex(int vertex) {
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    public void addEdge(int v1, int v2) {
        adjacencyList.putIfAbsent(v1, new ArrayList<>());
        adjacencyList.putIfAbsent(v2, new ArrayList<>());
        adjacencyList.get(v1).add(v2);
        adjacencyList.get(v2).add(v1); // Undirected graph
    }

    public void display() {
        for(Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
            System.out.print(entry.getKey() + " -> ");
            System.out.println(entry.getValue());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GraphExample graph = new GraphExample();

        boolean running = true;

        while(running) {
            System.out.println("\n=== Graph Operations ===");
            System.out.println("1. Add vertex");
            System.out.println("2. Add edge");
            System.out.println("3. Display graph");
            System.out.println("4. Exit");
            System.out.print("Choose option: ");

            int choice = scanner.nextInt();

            switch(choice) {
                case 1:
                    System.out.print("Enter vertex: ");
                    int vertex = scanner.nextInt();
                    graph.addVertex(vertex);
                    System.out.println("Vertex added!");
                    break;
                case 2:
                    System.out.print("Enter first vertex: ");
                    int v1 = scanner.nextInt();
                    System.out.print("Enter second vertex: ");
                    int v2 = scanner.nextInt();
                    graph.addEdge(v1, v2);
                    System.out.println("Edge added!");
                    break;
                case 3:
                    System.out.println("\nGraph adjacency list:");
                    graph.display();
                    break;
                case 4:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        }

        scanner.close();
    }
}
