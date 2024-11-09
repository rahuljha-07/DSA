#include <vector>
#include <queue>
using namespace std;

// Function to get the right view of a binary tree
vector<int> getRightView(Node* root) {
    vector<int> rightViewNodes; // Vector to store the right view nodes
    
    // If root is null, return an empty vector
    if (!root) return rightViewNodes;

    queue<Node*> nodeQueue; // Queue for level order traversal
    nodeQueue.push(root);

    while (!nodeQueue.empty()) {
        int levelSize = nodeQueue.size(); // Number of nodes at the current level
        
        // The first node in each level is part of the right view
        rightViewNodes.push_back(nodeQueue.front()->data);

        // Traverse all nodes at the current level
        while (levelSize--) {
            Node* currentNode = nodeQueue.front();
            nodeQueue.pop();
            
            // Add the right child to the queue if it exists
            if (currentNode->right) {
                nodeQueue.push(currentNode->right);
            }
            
            // Add the left child to the queue if it exists
            if (currentNode->left) {
                nodeQueue.push(currentNode->left);
            }
        }
    }
    
    return rightViewNodes;
}
