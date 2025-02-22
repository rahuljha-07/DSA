#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Structure for the priority queue elements (weight, node, parent)
typedef pair<int, pair<int, int>> QueueElement; // {weight, {node, parent}}

// Function to implement Prim's algorithm and print MST
void primMST(int N, vector<vector<pair<int, int>>>& adj) {
    // Min-heap priority queue to store {weight, {node, parent}}
    priority_queue<QueueElement, vector<QueueElement>, greater<QueueElement>> pq;

    vector<bool> visited(N, false); // To track visited nodes

    // Initial push (starting with node 0, weight = 0, parent = -1)
    pq.push({0, {0, -1}});

    cout << "Edges in the MST:" << endl;

    while (!pq.empty()) {
        // Extract the element with the smallest weight
        auto [weight, nodePair] = pq.top();
        int node = nodePair.first;   // Current node
        int parent = nodePair.second; // Parent of the current node
        pq.pop();

        // If the node is already visited, skip it
        if (visited[node]) continue;

        visited[node] = true; // Mark the node as visited

        // Print the edge if parent is not -1 (skip the initial push)
        if (parent != -1) {
            cout << parent << " - " << node << " with weight " << weight << endl;
        }

        // Traverse all adjacent nodes
        for (auto& [adjNode, adjWeight] : adj[node]) {
            if (!visited[adjNode]) {
                // Push {weight, {node, parent}} into the priority queue
                pq.push({adjWeight, {adjNode, node}});
            }
        }
    }
}

int main() {
    int N = 5; // Number of nodes
    vector<vector<pair<int, int>>> adj(N);

    // Adjacency list representation of the graph
    adj[0].push_back({1, 2}); // Edge 0-1 with weight 2
    adj[0].push_back({3, 6}); // Edge 0-3 with weight 6
    adj[1].push_back({0, 2}); // Edge 1-0 with weight 2
    adj[1].push_back({2, 3}); // Edge 1-2 with weight 3
    adj[1].push_back({3, 8}); // Edge 1-3 with weight 8
    adj[1].push_back({4, 5}); // Edge 1-4 with weight 5
    adj[2].push_back({1, 3}); // Edge 2-1 with weight 3
    adj[2].push_back({4, 7}); // Edge 2-4 with weight 7
    adj[3].push_back({0, 6}); // Edge 3-0 with weight 6
    adj[3].push_back({1, 8}); // Edge 3-1 with weight 8
    adj[4].push_back({1, 5}); // Edge 4-1 with weight 5
    adj[4].push_back({2, 7}); // Edge 4-2 with weight 7

    // Find and print the MST
    primMST(N, adj);

    return 0;
}
