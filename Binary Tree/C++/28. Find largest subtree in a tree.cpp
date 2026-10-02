#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

// Definition of a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Helper function to find the maximum subtree sum
int findLargestSubtreeSumUtil(Node* root, int& maxSum) {
    // Base case: if the current node is null, return 0 as sum
    if (!root) return 0;

    // Calculate the sum of nodes in the left and right subtrees
    int leftSubtreeSum = findLargestSubtreeSumUtil(root->left, maxSum);
    int rightSubtreeSum = findLargestSubtreeSumUtil(root->right, maxSum);

    // Sum of the current subtree rooted at this node
    int currentSubtreeSum = root->data + leftSubtreeSum + rightSubtreeSum;

    // Update maxSum if the current subtree sum is greater
    maxSum = max(maxSum, currentSubtreeSum);

    // Return the current subtree sum to the parent call
    return currentSubtreeSum;
}

// Main function to find the largest subtree sum in the tree
int findLargestSubtreeSum(Node* root) {
    int maxSum = INT_MIN;  // Initialize to the smallest possible integer
    findLargestSubtreeSumUtil(root, maxSum); // Recursively calculate subtree sums
    return maxSum;
}

// Example usage
int main() {
    // Create the binary tree for testing
    Node* root = new Node(1);
    root->left = new Node(-2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(-6);
    root->right->right = new Node(2);

    // Calculate and print the largest subtree sum
    int result = findLargestSubtreeSum(root);
    cout << "Largest subtree sum is: " << result << endl;

    return 0;
}
