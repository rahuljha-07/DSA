#include <vector>
#include <queue>
using namespace std;

// Function to get the left view of a binary tree
vector<int> getLeftView(Node* root) {
    vector<int> leftViewNodes; // Vector to store the left view nodes
    
    // If root is null, return an empty vector
    if (!root) return leftViewNodes;

    queue<Node*> nodeQueue; // Queue for level order traversal
    nodeQueue.push(root);

    while (!nodeQueue.empty()) {
        int levelSize = nodeQueue.size(); // Number of nodes at the current level
        
        // The first node in each level is part of the left view
        leftViewNodes.push_back(nodeQueue.front()->data);

        // Traverse all nodes at the current level
        while (levelSize--) {
            Node* currentNode = nodeQueue.front();
            nodeQueue.pop();
            
            // Add the left child to the queue if it exists
            if (currentNode->left) {
                nodeQueue.push(currentNode->left);
            }
            
            // Add the right child to the queue if it exists
            if (currentNode->right) {
                nodeQueue.push(currentNode->right);
            }
        }
    }
    
    return leftViewNodes;
}
