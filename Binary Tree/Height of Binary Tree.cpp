#include <algorithm>  // For max() function

// Definition for a binary tree node.
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to perform top-down traversal and calculate height
void calculateHeight(Node* root, int currentHeight, int& maxHeight) {
    if (root == nullptr) {
        // Update the maximum height when reaching a leaf node (no root)
        maxHeight = max(maxHeight, currentHeight);
        return;
    }

    // Recursively visit left and right subtrees, increasing height by 1 for each level
    calculateHeight(root->left, currentHeight + 1, maxHeight);
    calculateHeight(root->right, currentHeight + 1, maxHeight);
}

// Wrapper function to calculate the height of the binary tree using top-down approach
int height(Node* root) {
    int maxHeight = 0;  // Variable to store the maximum height
    calculateHeight(root, 1, maxHeight);  // Start with height 1 for the root
    return maxHeight;
}

// bottom up approach
// Helper function to calculate height from the bottom-up
int calculateHeightBottomUp(Node* root) {
    if (root == nullptr) {
        return 0;  // Base case: If the tree is empty, return height as 0
    }

    // Recursively calculate the height of left and right subtrees and return the maximum height + 1
    int leftHeight = calculateHeightBottomUp(root->left);
    int rightHeight = calculateHeightBottomUp(root->right);

    return 1 + max(leftHeight, rightHeight);  // Height is max of left and right subtrees + 1
}

// Main height function that calls the helper function
int height(Node* root) {
    // Call the helper function to calculate the height and return the result
    return calculateHeightBottomUp(root);
}