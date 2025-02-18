#include <iostream>
#include <algorithm>  // For std::swap
using namespace std;

// Definition for a binary tree node.
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Helper function to mirror a single node (swap its left and right children)
//top down approach
Node* mirror(Node* root) {
    if (root == nullptr) {
        return nullptr;
    }

    // Use swap to swap the left and right children
    swap(root->left, root->right);

    // Recursively mirror the left and right subtrees
    if (root->left) mirror(root->left);
    if (root->right) mirror(root->right);

    return root;
}

//bottom up
Node* mirror(Node* root) {
    if (root == nullptr) {
        return nullptr;
    }

    // Recursively mirror the left and right subtrees
    Node* leftMirror = mirror(root->left);
    Node* rightMirror = mirror(root->right);

    // Swap the mirrored subtrees
    root->left = rightMirror;
    root->right = leftMirror;

    return root;
}

// Function to create a mirror of the binary tree
Node* createMirror(Node* root) {
    // Call the helper function to mirror the tree
    Node* mirrorBinaryTree = mirror(root);

    return mirrorBinaryTree;  // Return the root of the mirrored tree
}

// Function to print inorder traversal of the tree (to check the result)
void inorder(Node* root) {
    if (root == nullptr) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int main() {
    // Create a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    cout << "Original tree (Inorder): ";
    inorder(root);
    cout << endl;

    // Create mirror of the tree
    Node* mirrorRoot = createMirror(root);

    cout << "Mirror tree (Inorder): ";
    inorder(mirrorRoot);
    cout << endl;

    return 0;
}
