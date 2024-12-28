#include <iostream>
using namespace std;

// Define the structure of a tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

int ans; // Global variable to track if all leaves are at the same level

// Helper function to check if all leaves are at the same level
void checkLeavesAtSameLevel(Node* root, int currentHeight, int& leafLevel) {
    // If the current node is null, return
    if (!root) return;

    // If the global answer flag is already set to 0 (false), return early
    if (ans == 0) return;

    // If the current node is a leaf node
    if (!root->left && !root->right) {
        // If this is the first leaf, set leafLevel to the current height
        if (leafLevel == -1) {
            leafLevel = currentHeight;
        }
        // If this is not the first leaf, check if it's at the same level
        else {
            if (leafLevel != currentHeight) {
                ans = 0; // Set answer flag to 0 if levels don't match
            }
        }
    }

    // Recursively check left and right subtrees
    checkLeavesAtSameLevel(root->left, currentHeight + 1, leafLevel);
    checkLeavesAtSameLevel(root->right, currentHeight + 1, leafLevel);
}

// Main function to check if all leaves in the binary tree are at the same level
bool check(Node* root) {
    ans = 1;          // Initialize answer flag to 1 (true)
    int leafLevel = -1; // Initialize leaf level to -1 (not set)

    // Call the helper function with the initial height of 0
    checkLeavesAtSameLevel(root, 0, leafLevel);

    return ans; // Return true if all leaves are at the same level, else false
}

// Example usage
int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    cout << "Are all leaves at the same level? " << (check(root) ? "Yes" : "No") << endl;

    return 0;
}
