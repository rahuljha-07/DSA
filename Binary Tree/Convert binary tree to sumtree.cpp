// Function to convert a binary tree into a sum tree
int convertToSumTree(Node* root) {
    // Base case: if the node is null, return 0 as sum
    if (!root) return 0;
    
    // Recursive calls to get the sum of left and right subtrees
    int leftSum = convertToSumTree(root->left);
    int rightSum = convertToSumTree(root->right);
    
    // Update the current node's data with the sum of curr data, left and right subtrees
    int newValue = root->data + leftSum + rightSum;
    
    // Return the sum of the current node and its updated subtrees
    return newValue;
}