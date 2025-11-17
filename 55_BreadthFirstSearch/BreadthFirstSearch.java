import java.util.*;

/**
 * BreadthFirstSearch - BFS graph traversal
 * Level-order traversal using queue
 */
public class BreadthFirstSearch {
    private Map<Integer, List<Integer>> adjacencyList;

    public BreadthFirstSearch() {
        adjacencyList = new HashMap<>();
    }

    public void addEdge(int v1, int v2) {
        adjacencyList.putIfAbsent(v1, new ArrayList<>());
        adjacencyList.putIfAbsent(v2, new ArrayList<>());
        adjacencyList.get(v1).add(v2);
    }

    public void bfs(int start) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(start);
        visited.add(start);

        System.out.println("BFS Traversal:");
        while(!queue.isEmpty()) {
            int vertex = queue.poll();
            System.out.print(vertex + " ");

            List<Integer> neighbors = adjacencyList.getOrDefault(vertex, new ArrayList<>());
            for(int neighbor : neighbors) {
                if(!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        BreadthFirstSearch graph = new BreadthFirstSearch();

        // Example graph
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 5);
        graph.addEdge(2, 6);

        System.out.println("=== Breadth First Search ===");
        graph.bfs(0);
    }
}
