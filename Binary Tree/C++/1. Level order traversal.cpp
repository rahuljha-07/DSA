// Function to perform level-order traversal (Breadth-First Search) of a binary tree
vector<int> levelOrderTraversal(Node* root) {
    // Initialize an empty vector to store the result
    vector<int> result;
    
    // If the tree is empty (root is null), return an empty vector
    if (root==nullptr) {
        return result;
    }
    
    // Queue to store nodes for level order processing
    queue<Node*> nodeQueue;
    
    // Start by pushing the root node into the queue
    nodeQueue.push(root);
    
    // Process nodes in the queue while it's not empty
    while (!nodeQueue.empty()) {
        // Get the front node in the queue
        Node* currentNode = nodeQueue.front();
        
        // Add the current node's data to the result vector
        result.push_back(currentNode->data);
        
        // Push the left child to the queue if it exists
        if (currentNode->left) {
            nodeQueue.push(currentNode->left);
        }
        
        // Push the right child to the queue if it exists
        if (currentNode->right) {
            nodeQueue.push(currentNode->right);
        }
        
        // Pop the processed node from the queue
        nodeQueue.pop();
    }
    
    // Return the final level-order traversal result
    return result;
}
