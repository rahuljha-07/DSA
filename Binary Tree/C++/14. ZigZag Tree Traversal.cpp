vector<int> zigZagTraversal(Node* root) {
    vector<int> result;  // To store the final zigzag order
    if (!root) return result;  // If the tree is empty, return an empty result
    
    queue<Node*> nodeQueue;  // Queue for level order traversal
    nodeQueue.push(root);  // Push the root node into the queue
    
    int level = 0;  // To alternate the traversal direction (even for left-to-right, odd for right-to-left)
    
    while (!nodeQueue.empty()) {
        int levelSize = nodeQueue.size();  // Number of nodes at the current level
        vector<int> currentLevelNodes;  // To store the nodes of the current level
        
        // Process all nodes at the current level
        while (levelSize--) {
            Node* currentNode = nodeQueue.front();
            nodeQueue.pop();
            currentLevelNodes.push_back(currentNode->data);  // Add the node's data to the current level's list
            
            // Enqueue the left and right children if they exist
            if (currentNode->left) nodeQueue.push(currentNode->left);
            if (currentNode->right) nodeQueue.push(currentNode->right);
        }
        
        // If it's an even level, add nodes as they are
        if (level % 2 == 0) {
            for (auto nodeData : currentLevelNodes) {
                result.push_back(nodeData);  // Append the node's data to the result
            }
        } 
        // If it's an odd level, reverse the nodes and add them to the result
        else {
            reverse(currentLevelNodes.begin(), currentLevelNodes.end());  // Reverse the nodes
            for (auto nodeData : currentLevelNodes) {
                result.push_back(nodeData);  // Append the reversed node's data to the result
            }
        }
        
        level++;  // Toggle the level to alternate the traversal direction
    }
    
    return result;  // Return the final zigzag traversal result
}
