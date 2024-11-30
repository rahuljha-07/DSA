#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>
using namespace std;

int minEdgesToReverse(int n, vector<pair<int, int>>& edges, int src, int dest) {
    // Step 1: Build the graph
    vector<vector<pair<int, int>>> graph(n + 1); // Adjacency list
    for (auto& edge : edges) {
        int u = edge.first, v = edge.second;
        // Add normal edge with weight 0
        graph[u].push_back({v, 0});
        // Add reversed edge with weight 1
        graph[v].push_back({u, 1});
    }

    // Step 2: Priority Queue for Dijkstra's Algorithm
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    vector<int> dist(n + 1, INT_MAX); // Distance array

    // Start from the source
    pq.push({0, src}); // {distance, node}
    dist[src] = 0;

    while (!pq.empty()) {
        auto [cost, node] = pq.top();
        pq.pop();

        // If this cost is already greater, skip
        if (cost > dist[node]) continue;

        // Explore neighbors
        for (auto& [neighbor, weight] : graph[node]) {
            if (cost + weight < dist[neighbor]) {
                dist[neighbor] = cost + weight;
                pq.push({dist[neighbor], neighbor});
            }
        }
    }

    // Step 3: Return the result
    return (dist[dest] == INT_MAX) ? -1 : dist[dest];
}

int main() {
    int n = 6; // Number of nodes
    vector<pair<int, int>> edges = {
        {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 1}
    };
    int src = 1, dest = 5;

    int result = minEdgesToReverse(n, edges, src, dest);
    if (result == -1) {
        cout << "Destination not reachable.\n";
    } else {
        cout << "Minimum edges to reverse: " << result << endl;
    }

    return 0;
}
