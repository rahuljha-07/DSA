#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Function to implement Bellman-Ford Algorithm
bool bellmanFord(int n, vector<vector<int>>& edges, int source, vector<int>& dist) {
    // Initialize distances from the source to all vertices
    dist.assign(n, INT_MAX); // Fill the distance array with infinity
    dist[source] = 0;        // Distance to the source is 0

    // Relax all edges (n-1) times
    for (int count = 1; count < n; count++) {
        for (const auto& edge : edges) {
            int src = edge[0];
            int dest = edge[1];
            int weight = edge[2];

            // Relax the edge if a shorter path is found
            if (dist[src] != INT_MAX && dist[src] + weight < dist[dest]) {
                dist[dest] = dist[src] + weight;
            }
        }
    }

    // Check for negative weight cycles by trying to relax the edges again
    for (const auto& edge : edges) {
        int src = edge[0];
        int dest = edge[1];
        int weight = edge[2];

        if (dist[src] != INT_MAX && dist[src] + weight < dist[dest]) {
            // Negative weight cycle detected
            return false;
        }
    }

    return true; // No negative weight cycles
}

int main() {
    int n, m; // Number of vertices and edges
    cin >> n >> m;

    vector<vector<int>> edges(m, vector<int>(3)); // Graph edges: {source, destination, weight}

    // Input edges
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    int source;
    cin >> source; // Input source vertex

    vector<int> dist; // To store shortest distances

    // Run Bellman-Ford Algorithm
    if (bellmanFord(n, edges, source, dist)) {
        cout << "Shortest distances from source " << source << ":\n";
        for (int i = 0; i < n; i++) {
            if (dist[i] == INT_MAX) {
                cout << "INF "; // If a vertex is unreachable
            } else {
                cout << dist[i] << " ";
            }
        }
        cout << endl;
    } else {
        cout << "Graph contains a negative weight cycle.\n";
    }

    return 0;
}
