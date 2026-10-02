#include <iostream>
#include <algorithm>
using namespace std;

// Definition of a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Helper function to find the maximum sum on the longest path
int findMaxSumPath(Node* root, int currentLength, int& maxLength, int currentSum, int& maxSum) {
    // Base case: if the current node is null, return 0
    if (!root) return 0;

    // Recursively calculate for left and right subtrees
    int leftSum = findMaxSumPath(root->left, currentLength + 1, maxLength, currentSum + root->data, maxSum);
    int rightSum = findMaxSumPath(root->right, currentLength + 1, maxLength, currentSum + root->data, maxSum);

    // Apply logic: Check the current path's length and sum to update maxLength and maxSum
    if (!root->left && !root->right) { // At a leaf node
        if (currentLength >= maxLength) {
            maxLength = currentLength;
            maxSum = max(maxSum, currentSum + root->data);
        }
    }

    // Return the maximum sum for this path
    return max(leftSum, rightSum);
}

// Main function to initiate the longest path sum calculation
int sumOfLongRootToLeafPath(Node* root) {
    if (!root) return 0; // Handle empty tree
    int maxLength = 0, maxSum = 0;
    findMaxSumPath(root, 1, maxLength, root->data, maxSum);
    return maxSum;
}


// Example usage
int main() {
    Node* root = new Node(4);
    root->left = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(7);
    root->left->right = new Node(1);
    root->right->left = new Node(2);
    root->right->right = new Node(3);
    root->left->right->left = new Node(6);

    int result = sumOfLongRootToLeafPath(root);
    cout << "Maximum sum of nodes on the longest path from root to leaf: " << result << endl;

    return 0;
}
