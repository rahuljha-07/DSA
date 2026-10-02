#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Function to check if the graph has an Eulerian path
bool hasEulerianPath(const vector<vector<int>>& graph, int& startNode) {
    int oddDegreeCount = 0;
    int n = graph.size();
    
    // Count nodes with odd degree
    for (int i = 0; i < n; i++) {
        int degree = 0;
        for (int j = 0; j < n; j++) {
            degree += graph[i][j];
        }
        if (degree % 2 != 0) {
            oddDegreeCount++;
            startNode = i; // Possible starting node
        }
    }
    
    // Eulerian path exists if there are 0 or 2 nodes with odd degree
    return (oddDegreeCount == 0 || oddDegreeCount == 2);
}

// Helper function to find Eulerian path
void findEulerianPath(vector<vector<int>>& graph, int startNode) {
    stack<int> currentPath;
    vector<int> eulerPath;
    currentPath.push(startNode);

    while (!currentPath.empty()) {
        int currentNode = currentPath.top();
        bool edgeFound = false;

        // Search for a connected edge
        for (int nextNode = 0; nextNode < graph.size(); nextNode++) {
            if (graph[currentNode][nextNode] > 0) {
                // Remove the edge from the graph
                graph[currentNode][nextNode]--;
                graph[nextNode][currentNode]--;
                currentPath.push(nextNode);
                edgeFound = true;
                break;
            }
        }

        if (!edgeFound) {
            // Backtrack and add to Euler path
            eulerPath.push_back(currentNode);
            currentPath.pop();
        }
    }

    // Print the Eulerian path
    for (int i = eulerPath.size() - 1; i >= 0; i--) {
        cout << eulerPath[i] + 1;
        if (i != 0) cout << " -> ";
    }
    cout << endl;
}

int main() {
    // Example input graph (adjacency matrix)
    vector<vector<int>> graph = {
        {0, 1, 0, 0, 1},
        {1, 0, 1, 1, 0},
        {0, 1, 0, 1, 0},
        {0, 1, 1, 0, 0},
        {1, 0, 0, 0, 0}
    };

    int startNode = 0;

    // Check if Eulerian path is possible
    if (hasEulerianPath(graph, startNode)) {
        cout << "Eulerian Path: ";
        findEulerianPath(graph, startNode);
    } else {
        cout << "No Solution" << endl;
    }

    return 0;
}
