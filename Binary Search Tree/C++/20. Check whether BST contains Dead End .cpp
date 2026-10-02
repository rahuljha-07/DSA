#include <iostream>
#include <climits>  // For INT_MAX
using namespace std;

// Structure for a binary search tree (BST) node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Helper function to recursively check for dead ends in the BST
void checkDeadEnd(Node* root, int minVal, int maxVal, bool &hasDeadEnd) {
    if (!root) return;  // Base case: If the node is null, return

    if (hasDeadEnd) return;  // If a dead end is already found, stop further checks

    // Check if the current node is a leaf node
    if (!root->left && !root->right) {
        // If the node's value is at the boundary of the valid range, it's a dead end
        if (minVal == maxVal) {
            hasDeadEnd = true;  // Mark that a dead end is found
            return;
        }
    }

    // Recursively check the left and right subtrees with updated ranges
    checkDeadEnd(root->left, minVal, root->data - 1, hasDeadEnd);  // Left child: range is (minVal, root->data-1)
    checkDeadEnd(root->right, root->data + 1, maxVal, hasDeadEnd); // Right child: range is (root->data+1, maxVal)
}

// Main function to check if the BST contains a dead end
bool isDeadEnd(Node* root) {
    bool hasDeadEnd = false;  // Flag to track if a dead end is found
    checkDeadEnd(root, 1, INT_MAX, hasDeadEnd);  // Initial call with the full range
    return hasDeadEnd;  // Return the result (true if a dead end is found, false otherwise)
}

int main() {
    // Example BST:
    //             8
    //          /     \
    //        5         9
    //      /   \     
    //    2       7 
    //   /  
    //  1 

    Node* root = new Node(8);
    root->left = new Node(5);
    root->right = new Node(9);
    root->left->left = new Node(2);
    root->left->right = new Node(7);
    root->left->left->left = new Node(1);

    // Check if the BST contains a dead end
    cout << "BST contains dead end? " << (isDeadEnd(root) ? "Yes" : "No") << endl;

    return 0;
}
