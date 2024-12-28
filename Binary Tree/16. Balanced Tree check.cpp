#include <iostream>
#include <algorithm>  // For max and abs functions
using namespace std;

// Definition of the binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Global variable to keep track of the balance status
int isBalancedFlag;

// Function to calculate the height of a tree while checking if it is balanced
int height(Node* root) {
    if (!root) return 0;  // If the node is NULL, its height is 0
    
    // Recursively calculate the height of the left and right subtrees
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    
    // If the difference between left and right subtree heights is greater than 1, it's not balanced
    if (abs(leftHeight - rightHeight) > 1) {
        isBalancedFlag = 0;  // Set the flag to false (0) if the tree is unbalanced
    }
    
    // Return the height of the current node
    return max(leftHeight, rightHeight) + 1;
}

// Function to check if the binary tree is balanced
bool isBalanced(Node* root) {
    isBalancedFlag = 1;  // Set the flag to true (1) initially
    height(root);  // Calculate the height and check the balance status
    return isBalancedFlag;  // Return the result based on the flag (1 = balanced, 0 = unbalanced)
}

// Helper function to print if the tree is balanced
void printBalanceStatus(Node* root) {
    if (isBalanced(root)) {
        cout << "The tree is balanced." << endl;
    } else {
        cout << "The tree is not balanced." << endl;
    }
}

// Main function to test the code
int main() {
    // Example 1: Balanced tree
    Node* root1 = new Node(1);
    root1->left = new Node(2);
    root1->right = new Node(3);
    root1->left->left = new Node(4);
    root1->left->right = new Node(5);
    root1->right->right = new Node(6);

    printBalanceStatus(root1);  // Output: The tree is balanced.

    // Example 2: Unbalanced tree
    Node* root2 = new Node(1);
    root2->left = new Node(2);
    root2->left->left = new Node(3);
    root2->left->left->left = new Node(4);

    printBalanceStatus(root2);  // Output: The tree is not balanced.

    return 0;
}
