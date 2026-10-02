#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <climits>
using namespace std;

// Perform topological sort using DFS
void topologicalSort(int node, vector<pair<int, int>> adj[], vector<bool> &visited, stack<int> &st) {
    visited[node] = true;
    for (auto &neighbor : adj[node]) {
        if (!visited[neighbor.first]) {
            topologicalSort(neighbor.first, adj, visited, st);
        }
    }
    st.push(node);
}

// Longest Path in a DAG using your approach
void findLongestPath(int V, vector<pair<int, int>> adj[], int source) {
    // Step 1: Perform topological sort
    stack<int> st;
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topologicalSort(i, adj, visited, st);
        }
    }

    // Step 2: Reverse the topological order
    vector<int> topoOrder;
    while (!st.empty()) {
        topoOrder.push_back(st.top());
        st.pop();
    }

    // Step 3: Initialize distances
    vector<int> dist(V, INT_MIN);
    dist[source] = 0;

    // Step 4: BFS using topological order
    for (int u : topoOrder) {
        if (dist[u] != INT_MIN) { // Process only reachable nodes
            for (auto &neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                dist[v] = max(dist[v], dist[u] + weight);
            }
        }
    }

    // Step 5: Output the longest distances
    cout << "Longest distances from source " << source << ":\n";
    for (int i = 0; i < V; i++) {
        if (dist[i] == INT_MIN) {
            cout << "Node " << i << ": No path\n";
        } else {
            cout << "Node " << i << ": " << dist[i] << "\n";
        }
    }
}

// Main function
int main() {
    int V = 6; // Number of vertices
    vector<pair<int, int>> adj[V];

    // Add edges with weights
    adj[0].push_back({1, 5});
    adj[0].push_back({2, 3});
    adj[1].push_back({3, 6});
    adj[1].push_back({2, 2});
    adj[2].push_back({4, 4});
    adj[2].push_back({5, 2});
    adj[2].push_back({3, 7});
    adj[3].push_back({5, 1});
    adj[4].push_back({5, 6});

    int source = 0; // Specify the source node
    findLongestPath(V, adj, source);

    return 0;
}
