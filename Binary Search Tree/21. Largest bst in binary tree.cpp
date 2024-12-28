#include <iostream>
#include <climits>
using namespace std;

// Structure to represent the information about a subtree
struct BSTInfo {
    bool isBST;   // Whether the current subtree is a BST
    int size;     // The size of the current BST (number of nodes)
    int mini;     // Minimum value in the current subtree
    int maxi;     // Maximum value in the current subtree
};

// Structure to represent a node in the binary tree
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Helper function to find the largest BST subtree in the binary tree
BSTInfo largestBSTSubtree(Node* root) {
    if (!root) {
        // If the current node is NULL, return an empty BST (size 0)
        return {true, 0, INT_MAX, INT_MIN};
    }

    // Recursively get the information about the left and right subtrees
    BSTInfo leftInfo = largestBSTSubtree(root->left);
    BSTInfo rightInfo = largestBSTSubtree(root->right);

    // If both left and right subtrees are BSTs and the current node satisfies BST properties
    if (leftInfo.isBST && rightInfo.isBST && leftInfo.maxi < root->data && rightInfo.mini > root->data) {
        // The current node is part of a BST
        return {
            true,
            leftInfo.size + rightInfo.size + 1, // Add current node
            min(root->data, leftInfo.mini),     // Update minimum value
            max(root->data, rightInfo.maxi)     // Update maximum value
        };
    } else {
        // If the current node doesn't form a BST, return the largest size of the BST found so far
        return {
            false,
            max(leftInfo.size, rightInfo.size), // Take the maximum of left or right subtree BST sizes
            -1,
            -1
        };
    }
}

// Function to get the size of the largest BST subtree
int largestBST(Node* root) {
    BSTInfo result = largestBSTSubtree(root); // Get the result from the helper function
    return result.size;  // Return the size of the largest BST
}

// Driver code to test the function
int main() {
    // Construct the binary tree
    // Example 1:
    //       1
    //      / \
    //     4   4
    //    / \
    //   6   8
    Node* root1 = new Node(1);
    root1->left = new Node(4);
    root1->right = new Node(4);
    root1->left->left = new Node(6);
    root1->left->right = new Node(8);

    cout << "Largest BST size in the first tree: " << largestBST(root1) << endl;

    // Example 2:
    //       6
    //      / \
    //     6   2
    //      \  / \
    //       2 1   3
    Node* root2 = new Node(6);
    root2->left = new Node(6);
    root2->right = new Node(2);
    root2->left->right = new Node(2);
    root2->right->left = new Node(1);
    root2->right->right = new Node(3);

    cout << "Largest BST size in the second tree: " << largestBST(root2) << endl;

    return 0;
}
