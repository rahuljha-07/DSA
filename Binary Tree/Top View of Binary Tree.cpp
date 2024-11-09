#include <vector>
#include <map>
#include <queue>
using namespace std;

// Function to get the top view of a binary tree
vector<int> getTopView(Node* root) {
    vector<int> topViewNodes; // Vector to store the top view nodes
    
    // If the root is null, return an empty vector
    if (!root) return topViewNodes;

    // Map to store the first node's data at each horizontal distance (HD)
    map<int, int> topViewMap;
    
    // Queue for level order traversal, storing each node with its HD
    queue<pair<Node*, int>> nodeQueue;
    nodeQueue.push({root, 0}); // Start with the root at horizontal distance 0

    while (!nodeQueue.empty()) {
        Node* currentNode = nodeQueue.front().first; // Current node
        int horizontalDistance = nodeQueue.front().second; // Horizontal distance of the node
        nodeQueue.pop();

        // If this HD is not already in the map, add the current node's data
        if (topViewMap.find(horizontalDistance) == topViewMap.end()) {
            topViewMap[horizontalDistance] = currentNode->data;
        }

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
    for (const auto& entry : topViewMap) {
        topViewNodes.push_back(entry.second);
    }

    return topViewNodes;
}
