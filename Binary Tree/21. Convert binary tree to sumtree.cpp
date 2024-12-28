// Function to convert the tree to a sum tree
int convertToSumTree(Node* root) {
    // Base case: If the node is null, return 0
    if (!root) return 0;

    // Recursively calculate the sum of the left and right subtrees
    int leftSum = convertToSumTree(root->left);
    int rightSum = convertToSumTree(root->right);

    // Store the original value of the current node
    int originalValue = root->data;

    // Update the node's value to the sum of its left and right subtree sums
    root->data = leftSum + rightSum;

    // Return the total sum including the original value of the node
    return originalValue + root->data;
}