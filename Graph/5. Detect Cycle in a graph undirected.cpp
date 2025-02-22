// DFS
bool dfsCycleUtil(int node, int parent, vector<vector<int>> &adj, vector<bool> &visited) {
    visited[node] = true;

    // Explore neighbors
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            // Recurse for unvisited neighbors
            if (dfsCycleUtil(neighbor, node, adj, visited)) {
                return true;
            }
        } else if (neighbor != parent) {
            // Cycle detected
            return true;
        }
    }

    return false;
}

bool dfsCycleDetection(int V, vector<vector<int>> &adj) {
    vector<bool> visited(V, false); // To track visited nodes

    // Loop to handle disconnected components
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            if (dfsCycleUtil(i, -1, adj, visited)) {
                return true;
            }
        }
    }

    // No cycle found
    return false;
}


bool bfsCycleDetection(int V, vector<vector<int>> &adj) {
    vector<bool> visited(V, false); // To track visited nodes
    queue<pair<int, int>> q;        // Queue to store {node, parent}

    // Loop to handle disconnected components
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            q.push({i, -1});
            visited[i] = true;

            while (!q.empty()) {
                auto [node, parent] = q.front();
                q.pop();

                // Explore neighbors
                for (int neighbor : adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push({neighbor, node});
                    } else if (neighbor != parent) {
                        // Cycle detected
                        return true;
                    }
                }
            }
        }
    }

    // No cycle found
    return false;
}
