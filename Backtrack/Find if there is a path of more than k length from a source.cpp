#include <bits/stdc++.h>
using namespace std;

// Function to perform DFS and check if there's a path with length >= k
bool dfs(vector<pair<int, int>> adj[], vector<bool>& visited, int src, int k) {
    // If the current distance becomes more than or equal to k, return true
    if (k <= 0) 
        return true;

    // Mark the current node as visited
    visited[src] = true;

    // Explore all neighbors of the current node
    for (auto neighbor : adj[src]) {
        int v = neighbor.first;    // Neighbor vertex
        int weight = neighbor.second; // Edge weight

        // If the neighbor is not visited, recurse
        if (!visited[v]) {
            // Check if there's a path with length >= k from this neighbor
            if (dfs(adj, visited, v, k - weight)) 
                return true;
        }
    }

    // Backtrack: Unmark the current node
    visited[src] = false;

    return false;
}

// Function to check if there is a simple path with length >= k
bool pathMoreThanK(int V, vector<pair<int, int>> adj[], int src, int k) {
    // Create a visited array to keep track of visited nodes
    vector<bool> visited(V, false);

    // Call the helper function to start the DFS
    return dfs(adj, visited, src, k);
}

int main() {
    // Number of vertices
    int V = 9;

    // Create an adjacency list for the graph
    vector<pair<int, int>> adj[V];

    // Add edges (u, v, weight)
    adj[0].push_back({1, 4});
    adj[0].push_back({7, 8});
    adj[1].push_back({0, 4});
    adj[1].push_back({7, 11});
    adj[1].push_back({2, 8});
    adj[2].push_back({1, 8});
    adj[2].push_back({8, 2});
    adj[2].push_back({5, 4});
    adj[2].push_back({3, 7});
    adj[3].push_back({2, 7});
    adj[3].push_back({4, 9});
    adj[3].push_back({5, 14});
    adj[4].push_back({3, 9});
    adj[4].push_back({5, 10});
    adj[5].push_back({2, 4});
    adj[5].push_back({3, 14});
    adj[5].push_back({4, 10});
    adj[5].push_back({6, 2});
    adj[6].push_back({5, 2});
    adj[6].push_back({8, 6});
    adj[6].push_back({7, 1});
    adj[7].push_back({0, 8});
    adj[7].push_back({1, 11});
    adj[7].push_back({8, 7});
    adj[7].push_back({6, 1});
    adj[8].push_back({2, 2});
    adj[8].push_back({6, 6});
    adj[8].push_back({7, 7});

    // Input source and k
    int src = 0, k = 58;

    // Check if a path exists
    if (pathMoreThanK(V, adj, src, k)) {
        cout << "True\n";
    } else {
        cout << "False\n";
    }

    return 0;
}
