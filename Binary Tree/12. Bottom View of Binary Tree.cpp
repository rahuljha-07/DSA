#include <vector>
#include <map>
#include <queue>
using namespace std;

// Function to get the bottom view of a binary tree
vector<int> getBottomView(Node* root) {
    vector<int> bottomViewNodes; // Vector to store the bottom view nodes
    
    // If the root is null, return an empty vector
    if (!root) return bottomViewNodes;

    // Map to store the last node's data at each horizontal distance (HD)
    map<int, int> bottomViewMap;
    
    // Queue for level order traversal, storing each node with its HD
    queue<pair<Node*, int>> nodeQueue;
    nodeQueue.push({root, 0}); // Start with the root at horizontal distance 0

    while (!nodeQueue.empty()) {
        Node* currentNode = nodeQueue.front().first; // Current node
        int horizontalDistance = nodeQueue.front().second; // Horizontal distance of the node
        nodeQueue.pop();

        // Update the map with the current node's data at this HD
        // This ensures that the last node encountered at each HD is stored
        bottomViewMap[horizontalDistance] = currentNode->data;

        // Add the left child with HD - 1 if it exists
        if (currentNode->left) {
            nodeQueue.push({currentNode->left, horizontalDistance - 1});
        }

        // Add the right child with HD + 1 if it exists
        if (currentNode->right) {
            nodeQueue.push({currentNode->right, horizontalDistance + 1});
        }
    }

    // Traverse the map and add the nodes in order of HD to the result
    for (const auto& entry : bottomViewMap) {
        bottomViewNodes.push_back(entry.second);
    }

    return bottomViewNodes;
}
