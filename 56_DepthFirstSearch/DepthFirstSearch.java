import java.util.*;

/**
 * DepthFirstSearch - DFS graph traversal
 * Recursive depth-first traversal
 */
public class DepthFirstSearch {
    private Map<Integer, List<Integer>> adjacencyList;

    public DepthFirstSearch() {
        adjacencyList = new HashMap<>();
    }

    public void addEdge(int v1, int v2) {
        adjacencyList.putIfAbsent(v1, new ArrayList<>());
        adjacencyList.putIfAbsent(v2, new ArrayList<>());
        adjacencyList.get(v1).add(v2);
    }

    public void dfs(int start) {
        Set<Integer> visited = new HashSet<>();
        System.out.println("DFS Traversal:");
        dfsRecursive(start, visited);
        System.out.println();
    }

    private void dfsRecursive(int vertex, Set<Integer> visited) {
        visited.add(vertex);
        System.out.print(vertex + " ");

        List<Integer> neighbors = adjacencyList.getOrDefault(vertex, new ArrayList<>());
        for(int neighbor : neighbors) {
            if(!visited.contains(neighbor)) {
                dfsRecursive(neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {
        DepthFirstSearch graph = new DepthFirstSearch();

        // Example graph
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 5);
        graph.addEdge(2, 6);

        System.out.println("=== Depth First Search ===");
        graph.dfs(0);
    }
}
