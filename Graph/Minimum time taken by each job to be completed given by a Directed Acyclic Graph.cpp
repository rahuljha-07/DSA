#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int v, e;
    cin >> v >> e; // Number of vertices and edges

    // Graph representation and indegree array
    vector<int> g[v + 1];           // Adjacency list
    vector<int> indegree(v + 1, 0); // Indegree of each node

    // Input edges
    for (int i = 0; i < e; i++) {
        int x, y;
        cin >> x >> y; // Edge from x to y
        g[x].push_back(y);
        indegree[y]++;
    }

    // Array to store the time for each job
    vector<int> ans(v + 1, 0);

    // Queue for topological sorting
    queue<int> q;

    // Initialize the queue with nodes having 0 indegree
    for (int i = 1; i <= v; i++) {
        if (indegree[i] == 0) {
            q.push(i);
            ans[i] = 1; // Jobs with no dependencies start at time 1
        }
    }

    // Process the graph
    while (!q.empty()) {
        int val = q.front();
        q.pop();

        // Traverse all neighbors
        for (auto x : g[val]) {
            indegree[x]--; // Reduce indegree of the neighbor
            if (indegree[x] == 0) {
                q.push(x); // Add to the queue if indegree becomes 0
                ans[x] = ans[val] + 1; // Update time for the job
            }
        }
    }

    // Output the minimum time for each job
    for (int i = 1; i <= v; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
