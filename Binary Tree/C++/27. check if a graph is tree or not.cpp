// check if it is connected or not using dfs
#include <iostream>
#include <vector>
using namespace std;

// Function to perform DFS and check for cycles
bool hasCycle(int node, int parent, vector<vector<int>>& adjList, vector<bool>& visited) {
    visited[node] = true; // Mark the current node as visited
    
    // Visit all adjacent nodes
    for (int neighbor : adjList[node]) {
        if (!visited[neighbor]) {
            // Recur for unvisited neighbors
            if (hasCycle(neighbor, node, adjList, visited)) {
                return true;
            }
        } else if (neighbor != parent) {
            // If an adjacent node is visited and not the parent of the current node, there’s a cycle
            return true;
        }
    }
    return false;
}

// Function to check if a graph is a tree
bool isTree(int V, vector<pair<int, int>>& edges) {
    // A tree must have exactly V-1 edges
    if (edges.size() != V - 1) return false;

    // Create an adjacency list for the graph
    vector<vector<int>> adjList(V);
    for (auto edge : edges) {
        adjList[edge.first].push_back(edge.second);
        adjList[edge.second].push_back(edge.first);
    }

    vector<bool> visited(V, false); // Visited array to mark visited nodes

    // Check for cycle starting from node 0
    if (hasCycle(0, -1, adjList, visited)) return false;

    // Check if all nodes are visited (ensuring the graph is connected)
    for (int i = 0; i < V; i++) {
        if (!visited[i]) return false;
    }

    return true; // If no cycles and the graph is connected, it’s a tree
}

int main() {
    int V = 5;
    vector<pair<int, int>> edges = {{0, 1}, {0, 2}, {1, 3}, {1, 4}};

    if (isTree(V, edges)) {
        cout << "The graph is a tree." << endl;
    } else {
        cout << "The graph is not a tree." << endl;
    }

    return 0;
}
