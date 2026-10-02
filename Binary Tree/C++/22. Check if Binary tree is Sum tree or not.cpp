// Function to check if a binary tree is a sum tree
int flag;
bool isSumTreeUtil(Node* root) {
    // Base case: if the node is null, return 0 as sum
    if (!root) return 0;
    
    // If it's a leaf node, return its data value
    if (!root->left && !root->right) return root->data;
    
    // If flag is set to 0, return immediately to break recursion
    if (flag == 0) return 0;
    
    // Recursive calls to get the sum of left and right subtrees
    int leftSum = isSumTreeUtil(root->left);
    int rightSum = isSumTreeUtil(root->right);
    
    // Check if the current node's data is equal to the sum of left and right subtrees
    if (leftSum + rightSum != root->data) flag = 0;
    
    // Return the sum of the current node and its subtrees
    return leftSum + rightSum + root->data;
}

// Main function to check if a binary tree is a sum tree
bool isSumTree(Node* root) {
    int flag = 1; // Initialize flag as true (1)
    isSumTreeUtil(root);
    return flag;
}
