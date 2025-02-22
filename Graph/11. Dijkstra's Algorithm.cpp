#include <iostream>
#include <vector>
#include <queue>
#include <climits> // For INT_MAX
using namespace std;

// Function to initialize the graph as an adjacency list
vector<vector<pair<int, int>>> initializeGraph(int n, int m) {
    // Create an adjacency list for the graph
    vector<vector<pair<int, int>>> adj(n + 1);

    // Input graph edges
    int u, v, wt;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> wt; // Edge from `u` to `v` with weight `wt`
        adj[u].push_back({v, wt});
        adj[v].push_back({u, wt}); // For undirected graph
    }

    return adj;
}

// Function to perform Dijkstra's algorithm and find the shortest paths
vector<int> dijkstra(int n, int source, const vector<vector<pair<int, int>>>& adj) {
    // Min-heap to store {distance, node} pairs
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // Distance array to store shortest distance from the source
    vector<int> distTo(n + 1, INT_MAX); // Initialize distances to infinity
    distTo[source] = 0;                 // Distance to the source is 0

    // Push the source node into the priority queue
    pq.push({0, source}); // {distance, node}

    // Implementing Dijkstra's algorithm
    while (!pq.empty()) {
        int currDist = pq.top().first;  // Current node's distance
        int currNode = pq.top().second; // Current node
        pq.pop();

        // Iterate over the neighbors of the current node
        for (const auto& it : adj[currNode]) {
            int nextNode = it.first;    // Neighbor node
            int edgeWeight = it.second; // Weight of the edge to the neighbor

            // If a shorter path to the neighbor is found
            if (distTo[nextNode] > currDist + edgeWeight) {
                distTo[nextNode] = currDist + edgeWeight;  // Update the shortest distance
                pq.push({distTo[nextNode], nextNode}); // Push the updated distance and node
            }
        }
    }

    return distTo;
}

int main() {
    int n, m, source;
    cin >> n >> m; // Input number of nodes (n) and edges (m)

    // Initialize the graph
    vector<vector<pair<int, int>>> adj = initializeGraph(n, m);

    // Input the source node
    cin >> source;

    // Perform Dijkstra's algorithm
    vector<int> distances = dijkstra(n, source, adj);

    // Print the shortest distances from the source
    cout << "The distances from source node " << source << " are:\n";
    for (int i = 1; i <= n; i++) {
        if (distances[i] == INT_MAX) {
            cout << "INF "; // If node is unreachable, print INF
        } else {
            cout << distances[i] << " ";
        }
    }
    cout << "\n";

    return 0;
}
