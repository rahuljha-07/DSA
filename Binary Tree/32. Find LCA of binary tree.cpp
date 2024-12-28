#include <iostream>
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

// Internal helper function to find the LCA of two nodes
Node* findLCAHelper(Node* root, int n1, int n2) {
    // Base case: if root is null, return null
    if (!root) return nullptr;

    // If root matches either n1 or n2, it is part of the LCA
    if (root->data == n1 || root->data == n2) return root;

    // Recursively find LCA in the left and right subtrees
    Node* leftLCA = findLCAHelper(root->left, n1, n2);
    Node* rightLCA = findLCAHelper(root->right, n1, n2);

    // If both sides return non-null, this node is the LCA
    if (leftLCA && rightLCA) return root;

    // Otherwise, return the non-null side (either leftLCA or rightLCA)
    return leftLCA ? leftLCA : rightLCA;
}

// Public function to find the LCA by calling the helper function
Node* findLCA(Node* root, int n1, int n2) {
    return findLCAHelper(root, n1, n2);
}

int main() {
    // Example binary tree:
    //             1
    //          /     \
    //        2         3
    //      /   \     /   \
    //    4       5  6       7

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    int n1 = 4, n2 = 5;
    Node* lca = findLCA(root, n1, n2);
    if (lca) cout << "LCA of " << n1 << " and " << n2 << " is " << lca->data << endl;
    else cout << "LCA not found." << endl;

    return 0;
}
