#include <vector>
#include <queue>
using namespace std;

// function is same for both directed and unidrected graph
vector<int> bfsOfGraph(vector<vector<int>> &adj) {
    int V = adj.size(); // Number of vertices
    vector<int> bfs;    // To store BFS traversal
    vector<bool> visited(V, false); // To track visited nodes
    queue<int> q;

    // Start BFS from node 0
    q.push(0);
    visited[0] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        bfs.push_back(node);

        // Visit all unvisited neighbors
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    return bfs;
}
