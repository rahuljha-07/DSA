#include <iostream>
#include <vector>
#include <utility>
using namespace std;

// Function to perform DFS
bool dfs(int node, int k, vector<pair<int, int>> graph[], vector<bool>& visited) {
    // If the accumulated path length exceeds k, return true
    if (k <= 0) return true;

    // Mark the current node as visited
    visited[node] = true;

    // Explore all neighbors
    for (auto& neighbor : graph[node]) {
        int nextNode = neighbor.first;
        int weight = neighbor.second;

        // If the neighbor is not visited
        if (!visited[nextNode]) {
            // Recursive call to explore deeper paths
            if (dfs(nextNode, k - weight, graph, visited)) {
                return true;
            }
        }
    }

    // Backtrack: Unmark the current node as visited
    visited[node] = false;

    return false; // No valid path found
}

bool isPathMoreThanK(int n, int k, int src, vector<pair<int, int>> graph[]) {
    // Initialize visited array
    vector<bool> visited(n, false);

    // Perform DFS from the source
    return dfs(src, k, graph, visited);
}

int main() {
    // Number of vertices and edges
    int n = 9; // Number of vertices (0 to 8)
    int k = 58; // Minimum path length to check
    vector<pair<int, int>> graph[n];

    // Add edges to the graph (u, v, w)
    graph[0].push_back({7, 20});
    graph[7].push_back({0, 20});

    graph[7].push_back({1, 10});
    graph[1].push_back({7, 10});

    graph[1].push_back({2, 10});
    graph[2].push_back({1, 10});

    graph[2].push_back({3, 10});
    graph[3].push_back({2, 10});

    graph[3].push_back({4, 10});
    graph[4].push_back({3, 10});

    graph[4].push_back({5, 10});
    graph[5].push_back({4, 10});

    graph[5].push_back({6, 10});
    graph[6].push_back({5, 10});

    graph[6].push_back({8, 10});
    graph[8].push_back({6, 10});

    // Check if a path of length >= k exists
    if (isPathMoreThanK(n, k, 0, graph)) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }

    return 0;
}
