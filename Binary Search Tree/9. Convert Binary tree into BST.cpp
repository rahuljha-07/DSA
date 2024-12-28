#include <iostream>
#include <vector>
#include <algorithm> // For sorting
using namespace std;

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

// Helper function to perform an in-order traversal of the tree and store the values in a vector
void inOrderTraversal(Node* root, vector<int>& values) {
    if (!root) return;  // Base case: if the node is null, do nothing
    
    // Traverse the left subtree
    inOrderTraversal(root->left, values);
    
    // Add the node's data to the vector
    values.push_back(root->data);
    
    // Traverse the right subtree
    inOrderTraversal(root->right, values);
}

// Helper function to perform an in-order traversal of the tree and assign sorted values from the vector
void assignSortedValues(Node* root, vector<int>& values) {
    if (!root) return;  // Base case: if the node is null, do nothing
    
    // Traverse the left subtree
    assignSortedValues(root->left, values);
    
    // Assign the current node the next sorted value from the vector
    root->data = values[0];
    values.erase(values.begin());  // Remove the first element since it's been used
    
    // Traverse the right subtree
    assignSortedValues(root->right, values);
}

// Main function to convert a Binary Tree to a Binary Search Tree (BST)
Node* binaryTreeToBST(Node* root) {
    vector<int> values;
    
    // Step 1: Perform an in-order traversal of the binary tree to collect all values
    inOrderTraversal(root, values);
    
    // Step 2: Sort the values to ensure they can form a BST
    sort(values.begin(), values.end());
    
    // Step 3: Assign the sorted values back to the tree nodes in in-order traversal
    assignSortedValues(root, values);
    
    // Return the root of the modified tree, now a BST
    return root;
}

int main() {
    // Example Binary Tree:
    //             10
    //          /     \
    //        30         20
    //      /   \       /   \
    //    40      60  50    70

    Node* root = new Node(10);
    root->left = new Node(30);
    root->right = new Node(20);
    root->left->left = new Node(40);
    root->left->right = new Node(60);
    root->right->left = new Node(50);
    root->right->right = new Node(70);

    // Convert the binary tree to a BST
    Node* bstRoot = binaryTreeToBST(root);

    // Print the in-order traversal of the BST
    // This should print the sorted values in ascending order
    vector<int> result;
    inOrderTraversal(bstRoot, result);
    cout << "In-order traversal of the BST: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
