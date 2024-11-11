#include <iostream>
using namespace std;

// Definition for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to count the number of nodes in the binary tree
int size(Node* root) {
    if (root == nullptr) return 0;  // If the tree is empty, return 0
    int leftsize = size(root->left);
    int rightsize = size(root->right);
    return 1 + leftsize + rightsize;  // Recursively count nodes in left and right subtrees
}

// Helper function to check if the tree satisfies the heap property
bool solve(Node* tree, int n, int idx) {
    // Base case: If the node is null, it's valid
    if (tree == nullptr) return true;

    // If the current index exceeds the total number of nodes, it's not a valid heap
    if (idx >= n) return false;

    // Check if the current node satisfies the max-heap property
    if (tree->left && tree->left->data >= tree->data) return false;  // Left child should be smaller than the node
    if (tree->right && tree->right->data >= tree->data) return false;  // Right child should be smaller than the node

    // Recursively check the left and right subtrees
    return solve(tree->left, n, 2 * idx + 1) && solve(tree->right, n, 2 * idx + 2);
}

// Function to check if a binary tree is a max-heap
bool isHeap(Node* tree) {
    if (tree == nullptr) return true;  // An empty tree is trivially a heap

    int n = size(tree);  // Get the total number of nodes in the tree
    int idx = 0;  // Start from the root with index 0

    // Check if the tree satisfies both the complete binary tree and max-heap properties
    return solve(tree, n, idx);
}

// Test the function
int main() {
    // Creating a sample binary tree
    Node* root = new Node(10);
    root->left = new Node(5);
    root->right = new Node(2);
    root->left->left = new Node(3);
    root->left->right = new Node(4);
    root->right->left = new Node(1);

    if (isHeap(root)) {
        cout << "The binary tree is a max-heap." << endl;
    } else {
        cout << "The binary tree is not a max-heap." << endl;
    }

    return 0;
}
