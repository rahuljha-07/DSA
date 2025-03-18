#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// Function to clone the graph using BFS
Node* cloneGraph(Node* node) {
    if (node == nullptr) return nullptr;

    unordered_map<Node*, Node*> map; // Keeps track of cloned nodes
    queue<Node*> queue; // BFS queue

    // Clone the first node and add it to queue
    queue.push(node);
    map[node] = new Node(node->val);

    // BFS traversal
    while (!queue.empty()) {
        Node* current = queue.front();
        queue.pop();

        // Process all neighbors
        for (Node* neighbor : current->neighbors) {
            if (map.find(neighbor) == map.end()) { // If not cloned yet
                map[neighbor] = new Node(neighbor->val); // Clone it
                queue.push(neighbor); // Add to queue for processing
            }
            // Link the cloned node to its cloned neighbors
            map[current]->neighbors.push_back(map[neighbor]);
        }
    }

    return map[node]; // Return the cloned graph's entry point
}

// Function to print a graph (for debugging)
void printGraph(Node* node, unordered_map<Node*, bool>& visited) {
    if (node == nullptr || visited[node]) return;

    // Mark node as visited
    visited[node] = true;

    // Print the node and its neighbors
    cout << "Node " << node->val << " -> { ";
    for (Node* neighbor : node->neighbors) {
        cout << neighbor->val << " ";
    }
    cout << "}" << endl;

    // Recursively print neighbors
    for (Node* neighbor : node->neighbors) {
        printGraph(neighbor, visited);
    }
}

// Main function to test cloning
int main() {
    // Create the original graph:
    //      1
    //     / \
    //    2   3
    //     \ /
    //      4
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    Node* node3 = new Node(3);
    Node* node4 = new Node(4);

    node1->neighbors = {node2, node3};
    node2->neighbors = {node1, node4, node3};
    node3->neighbors = {node1, node2, node4};
    node4->neighbors = {node2, node3};

    // Print original graph
    cout << "Original Graph:\n";
    unordered_map<Node*, bool> visited;
    printGraph(node1, visited);

    // Clone the graph
    Node* clonedGraph = cloneGraph(node1);

    // Print cloned graph
    cout << "\nCloned Graph:\n";
    unordered_map<Node*, bool> visitedCloned;
    printGraph(clonedGraph, visitedCloned);

    return 0;
}



//DFS
class Solution {
public:
    // Helper function to perform DFS and clone the graph
    Node* dfsClone(Node* currentNode, unordered_map<Node*, Node*>& clonedNodes) {
        // Create a clone of the current node
        Node* cloneNode = new Node(currentNode->val);
        
        // Store the mapping of the current node to its clone
        clonedNodes[currentNode] = cloneNode;
        
        // Traverse all the neighbors of the current node
        for (Node* neighbor : currentNode->neighbors) {
            // If the neighbor is already cloned, add it to the current node's clone's neighbors
            if (clonedNodes.find(neighbor) != clonedNodes.end()) {
                cloneNode->neighbors.push_back(clonedNodes[neighbor]);
            } 
            // If the neighbor is not yet cloned, clone it recursively and add it
            else {
                cloneNode->neighbors.push_back(dfsClone(neighbor, clonedNodes));
            }
        }
        
        // Return the clone of the current node
        return cloneNode;
    }

    // Main function to clone the graph
    Node* cloneGraph(Node* node) {
        // Handle the edge case where the graph is empty
        if (node == nullptr) {
            return nullptr;
        }
        
        // A map to keep track of visited nodes and their clones
        unordered_map<Node*, Node*> clonedNodes;

        // Start DFS from the given node
        return dfsClone(node, clonedNodes);
    }
};
