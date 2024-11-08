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
void findMaxSumPath(Node* root, int currentLength, int currentSum, int& maxLength, int& maxSum) {
    // Base case: if the current node is null, return
    if (!root) return;

    // Recur for left and right subtrees with updated path length and sum
    if (root->left==nullptr && root->right==nullptr) { 
        // Check if this is the longest or max-sum path at the leaf node or If this path is as long as the longest path but has a higher sum, update maxSum
        if (currentLength >= maxLength) {
            maxLength = currentLength;
            maxSum = max(maxSum, currentSum);
        }
        return;
    }

    // Recur for left and right subtrees with updated path length and sum
    findMaxSumPath(root->left, currentLength + 1, currentSum + root->data, maxLength, maxSum);
    findMaxSumPath(root->right, currentLength + 1, currentSum + root->data, maxLength, maxSum);
}

// Main function to initiate the longest path sum calculation
int sumOfLongRootToLeafPath(Node* root) {
    int maxLength = 0, maxSum = 0;
    findMaxSumPath(root, 1, root->data, maxLength, maxSum);
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
