#include <iostream>
using namespace std;

// Global variable for ancestor
int ancestor = -1;

// Structure for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Helper function to find Kth ancestor
bool findKthAncestor(Node* root, int node, int& K) {
    // Base case: If the node is null, return false
    if (root == nullptr) return false;

    // If we found the node, return true (start going back up)
    if (root->data == node) return true;

    // Check both left and right subtrees
    bool foundInLeft = findKthAncestor(root->left, node, K);
    bool foundInRight = findKthAncestor(root->right, node, K);

    // If either left or right subtree contains the node
    if (foundInLeft || foundInRight) {
        // Decrease K because we are going back up the tree
        K--;

        // If K becomes 0, we found the Kth ancestor
        if (K == 0) {
            ancestor = root->data;
            return false; // stop further recursion
        }

        return true; // Continue looking for the Kth ancestor
    }

    return false; // Node is not found in either subtree
}

// Function to find Kth ancestor of a given node
int kthAncestor(Node* root, int node, int K) {
    ancestor = -1; // Reset the global ancestor variable
    findKthAncestor(root, node, K);
    return ancestor; // Return the ancestor
}

int main() {
    // Sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    int node = 5; // Find the 2nd ancestor of node 5
    int K = 2;

    int result = kthAncestor(root, node, K);
    if (result == -1) {
        cout << "No such ancestor exists." << endl;
    } else {
        cout << "The " << K << "th ancestor is: " << result << endl;
    }

    return 0;
}
