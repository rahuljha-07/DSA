#include <vector>
#include <queue>
#include <algorithm>  // For reverse()

// Definition for a binary tree node.
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to perform Reverse Level Order Traversal
vector<int> reverseLevelOrderTraversal(Node* root) {
    vector<int> result;  // To store the final result of reverse level-order traversal
    if (!root) return result;  // If the tree is empty, return an empty result
    
    queue<Node*> nodeQueue;  // Queue for level-order traversal
    nodeQueue.push(root);  // Start with the root node
    
    // Process nodes level by level
    while (!nodeQueue.empty()) {
        Node* currentNode = nodeQueue.front();  // Get the node at the front of the queue
        nodeQueue.pop();  // Remove the node from the queue
        
        result.push_back(currentNode->data);  // Add current node's data to the result
        
        // Enqueue right child first, then left child
        // This ensures that the left child is processed last (for reverse level-order)
        if (currentNode->right) {
            nodeQueue.push(currentNode->right);
        }
        if (currentNode->left) {
            nodeQueue.push(currentNode->left);
        }
    }
    
    // Reverse the result vector to get reverse level-order traversal
    reverse(result.begin(), result.end());
    
    return result;  // Return the reversed level-order traversal result
}
