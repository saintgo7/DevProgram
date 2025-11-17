import java.util.*;

/**
 * DijkstraAlgorithm - Shortest path algorithm
 * Finds shortest path in weighted graph
 */
public class DijkstraAlgorithm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Dijkstra's Algorithm ===");
        System.out.print("Enter number of vertices: ");
        int n = scanner.nextInt();

        int[][] graph = new int[n][n];

        System.out.println("Enter adjacency matrix (0 for no edge):");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                graph[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Enter source vertex (0-" + (n-1) + "): ");
        int source = scanner.nextInt();

        dijkstra(graph, source);

        scanner.close();
    }

    private static void dijkstra(int[][] graph, int src) {
        int n = graph.length;
        int[] dist = new int[n];
        boolean[] visited = new boolean[n];

        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        for(int count = 0; count < n - 1; count++) {
            int u = minDistance(dist, visited);
            visited[u] = true;

            for(int v = 0; v < n; v++) {
                if(!visited[v] && graph[u][v] != 0 &&
                   dist[u] != Integer.MAX_VALUE &&
                   dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }

        System.out.println("\nVertex\tDistance from Source");
        for(int i = 0; i < n; i++) {
            System.out.println(i + "\t\t" + dist[i]);
        }
    }

    private static int minDistance(int[] dist, boolean[] visited) {
        int min = Integer.MAX_VALUE, minIndex = -1;

        for(int v = 0; v < dist.length; v++) {
            if(!visited[v] && dist[v] <= min) {
                min = dist[v];
                minIndex = v;
            }
        }

        return minIndex;
    }
}
