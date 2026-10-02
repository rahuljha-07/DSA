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

    // If the answer is already false, no need to proceed further
    if (ans == 0) return;

    // First recursively check the left and right subtrees
    checkLeavesAtSameLevel(root->left, currentHeight + 1, leafLevel);
    checkLeavesAtSameLevel(root->right, currentHeight + 1, leafLevel);

    // After checking children, process the current node
    // If it's a leaf node
    if (!root->left && !root->right) {
        // If it's the first leaf found, record its level
        if (leafLevel == -1) {
            leafLevel = currentHeight;
        }
        // If it's not the first leaf, compare level with the first leaf's level
        else if (leafLevel != currentHeight) {
            ans = 0; // Set answer to false if leaf levels don't match
        }
    }
}

// Main function to check if all leaves in the binary tree are at the same level
bool check(Node* root) {
    ans = 1;           // Initialize answer flag to true
    int leafLevel = -1; // Leaf level initially not set

    checkLeavesAtSameLevel(root, 0, leafLevel); // Start from height 0

    return ans; // Return the final result
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
