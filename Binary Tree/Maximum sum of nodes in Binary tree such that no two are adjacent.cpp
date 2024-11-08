#include <iostream>
#include <unordered_map>
using namespace std;

// Definition of a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Memoization map to store the maximum sum for each subtree
unordered_map<Node*, int> memo;

// Recursive function to find the maximum sum of non-adjacent nodes
int getMaxSum(Node* root) {
    // Base case: If the current node is null, return 0 as there’s no value to add
    if (!root) return 0;

    // If the result for this node is already calculated, return it from the memo map
    if (memo.find(root) != memo.end()) return memo[root];

    // Include the current node's value in the sum
    int includeCurrent = root->data;

    // If the left child exists, add the maximum sum from the left child's grandchildren
    if (root->left) {
        includeCurrent += getMaxSum(root->left->left);
        includeCurrent += getMaxSum(root->left->right);
    }

    // If the right child exists, add the maximum sum from the right child's grandchildren
    if (root->right) {
        includeCurrent += getMaxSum(root->right->left);
        includeCurrent += getMaxSum(root->right->right);
    }

    // Exclude the current node's value, and instead take the maximum sum of its left and right subtrees
    int excludeCurrent = getMaxSum(root->left) + getMaxSum(root->right);

    // Return the maximum sum for the current node
    return memo[root] max(includeCurrent, excludeCurrent);
}

// Example usage
int main() {
    Node* root = new Node(10);
    root->left = new Node(1);
    root->left->left = new Node(2);
    root->left->right = new Node(3);
    root->right = new Node(4);
    root->right->right = new Node(5);

    cout << "Maximum sum of non-adjacent nodes: " << getMaxSum(root) << endl;

    return 0;
}
