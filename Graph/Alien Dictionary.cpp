#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;

// Helper function to perform DFS and store nodes in topological order
void topoSortUtil(int node, vector<int> adj[], vector<bool>& visited, stack<int>& topoStack) {
    visited[node] = true;  // Mark the node as visited

    // Explore all neighbors
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            topoSortUtil(neighbor, adj, visited, topoStack);
        }
    }

    // Push the node into the stack after exploring all its neighbors
    topoStack.push(node);
}

// Function to perform topological sorting
string topologicalSort(vector<int> adj[], int K) {
    vector<bool> visited(K, false); // To track visited nodes
    stack<int> topoStack;           // Stack to store topological order

    // Perform DFS for all unvisited nodes
    for (int i = 0; i < K; i++) {
        if (!visited[i]) {
            topoSortUtil(i, adj, visited, topoStack);
        }
    }

    // Extract nodes from the stack to get the topological order
    string topoOrder;
    while (!topoStack.empty()) {
        topoOrder += (char)('a' + topoStack.top());
        topoStack.pop();
    }

    return topoOrder;
}

// Function to find the order of characters in the alien dictionary
string findOrder(string words[], int N, int K) {
    vector<int> adj[K]; // Graph with K nodes (representing the alphabet)

    // Build the graph based on the given words
    for (int i = 0; i < N - 1; i++) {
        string word1 = words[i];
        string word2 = words[i + 1];

        // Compare characters of both words
        for (int j = 0; j < min(word1.size(), word2.size()); j++) {
            if (word1[j] != word2[j]) {
                int index1 = word1[j] - 'a'; // Character index in the alphabet
                int index2 = word2[j] - 'a';
                adj[index1].push_back(index2); // Add a directed edge
                break; // Only the first differing character determines the order
            }
        }
    }

    // Perform topological sort to find the order of characters
    return topologicalSort(adj, K);
}

int main() {
    // Example input
    int N = 5, K = 4;
    string words[] = {"baa", "abcd", "abca", "cab", "cad"};

    // Find the order of characters in the alien language
    string order = findOrder(words, N, K);
    cout << "The order of characters in the alien dictionary: " << order << endl;

    return 0;
}
