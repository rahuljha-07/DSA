#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Function to initialize the graph and indegree array
void initializeGraph(int v, int e, vector<vector<int>>& adj, vector<int>& indegree) {
    int x, y;
    for (int i = 0; i < e; i++) {
        cin >> x >> y; // Edge from x to y
        adj[x].push_back(y);
        indegree[y]++;
    }
}

// Function to perform topological sorting and calculate job times
vector<int> calculateJobTimes(int v, const vector<vector<int>>& adj, vector<int>& indegree) {
    vector<int> jobTime(v + 1, 0); // Stores the minimum time to start each job
    queue<int> q;

    // Push all nodes with 0 indegree to the queue
    for (int i = 1; i <= v; i++) {
        if (indegree[i] == 0) {
            q.push(i);
            jobTime[i] = 1; // Jobs with no dependencies can start immediately
        }
    }

    // Perform topological sorting and calculate job completion times
    while (!q.empty()) {
        int currentNode = q.front();
        q.pop();

        for (int neighbor : adj[currentNode]) {
            indegree[neighbor]--;

            if (indegree[neighbor] == 0) {
                q.push(neighbor);
                jobTime[neighbor] = jobTime[currentNode] + 1;
            }
        }
    }

    return jobTime;
}

// Function to display job completion times
void displayJobTimes(const vector<int>& jobTime) {
    for (size_t i = 1; i < jobTime.size(); i++) {
        cout << jobTime[i] << " ";
    }
    cout << endl;
}

int main() {
    int v, e;
    cin >> v >> e; // Number of vertices and edges

    // Graph representation and indegree array
    vector<vector<int>> adj(v + 1); // Adjacency list
    vector<int> indegree(v + 1, 0); // Indegree of each node

    // Initialize the graph
    initializeGraph(v, e, adj, indegree);

    // Calculate the minimum time required for each job
    vector<int> jobTime = calculateJobTimes(v, adj, indegree);

    // Display the results
    displayJobTimes(jobTime);

    return 0;
}
