#include <iostream>
#include <vector>
#include <queue>
#include <climits> // For INT_MAX
#include <algorithm> // For reverse
using namespace std;

// Function to initialize the graph as an adjacency list
vector<vector<pair<int, int>>> initializeGraph(int n, int m) {
    vector<vector<pair<int, int>>> adj(n + 1);

    int u, v, wt;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> wt;
        adj[u].push_back({v, wt});
        adj[v].push_back({u, wt}); // For undirected graph
    }

    return adj;
}

// Function to get the shortest path from source to a destination using the parent array
vector<int> getPath(int destination, const vector<int>& parent) {
    if (parent[destination] == -1) {
        return {-1}; // Destination is unreachable
    }

    vector<int> path;
    int node = destination;

    while (parent[node] != node) {
        path.push_back(node);
        node = parent[node];
    }

    path.push_back(node); // Include the source node
    reverse(path.begin(), path.end());
    return path;
}

// Dijkstra's algorithm to find the shortest paths from the source
pair<vector<int>, vector<int>> dijkstra(int n, int source, const vector<vector<pair<int, int>>>& adj) {
    vector<int> distTo(n + 1, INT_MAX);
    vector<int> parent(n + 1, -1);

    distTo[source] = 0;
    parent[source] = source;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        int currDist = pq.top().first;
        int currNode = pq.top().second;
        pq.pop();

        for (const auto& it : adj[currNode]) {
            int nextNode = it.first;
            int edgeWeight = it.second;

            if (distTo[nextNode] > currDist + edgeWeight) {
                distTo[nextNode] = currDist + edgeWeight;
                parent[nextNode] = currNode;
                pq.push({distTo[nextNode], nextNode});
            }
        }
    }

    return {distTo, parent};
}

int main() {
    int n, m, source;
    cin >> n >> m;

    vector<vector<pair<int, int>>> adj = initializeGraph(n, m);

    cin >> source;

    auto [distances, parents] = dijkstra(n, source, adj);

    // Display shortest distances
    cout << "The distances from source node " << source << " are:\n";
    for (int i = 1; i <= n; i++) {
        if (distances[i] == INT_MAX) {
            cout << "INF ";
        } else {
            cout << distances[i] << " ";
        }
    }
    cout << "\n";

    // Display shortest paths
    cout << "Shortest paths from source node " << source << " to all nodes:\n";
    for (int i = 1; i <= n; i++) {
        if (distances[i] != INT_MAX) {
            vector<int> path = getPath(i, parents);
            if (path[0] == -1) {
                cout << "No path to node " << i << "\n";
            } else {
                cout << "Path to node " << i << ": ";
                for (int p : path) {
                    cout << p << " ";
                }
                cout << "\n";
            }
        } else {
            cout << "Node " << i << " is unreachable from the source.\n";
        }
    }

    return 0;
}
