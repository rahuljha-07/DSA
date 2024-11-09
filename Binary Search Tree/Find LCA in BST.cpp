#include <iostream>
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

// Helper function to find LCA in a BST using recursive approach
Node* findLCAHelper(Node* root, int n1, int n2) {
    // Base case: if root is null, return null
    if (!root) return nullptr;

    // If both n1 and n2 are smaller than root's data, LCA lies in the left subtree
    if (root->data > n1 && root->data > n2) {
        return findLCAHelper(root->left, n1, n2);
    }
    // If both n1 and n2 are greater than root's data, LCA lies in the right subtree
    else if (root->data < n1 && root->data < n2) {
        return findLCAHelper(root->right, n1, n2);
    }
    
    // If one of n1 or n2 is on one side and the other is on the other side,
    // or if we find one of the nodes, then root is the LCA
    return root;
}

// Public function to find the LCA by calling the helper function
Node* findLCA(Node* root, int n1, int n2) {
    return findLCAHelper(root, n1, n2);
}

int main() {
    // Example BST:
    //             5
    //          /     \
    //        3         8
    //      /   \     /   \
    //    2       4  6     9

    Node* root = new Node(5);
    root->left = new Node(3);
    root->right = new Node(8);
    root->left->left = new Node(2);
    root->left->right = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(9);

    int n1 = 2, n2 = 4;
    Node* lca = findLCA(root, n1, n2);
    if (lca) cout << "LCA of " << n1 << " and " << n2 << " is " << lca->data << endl;
    else cout << "LCA not found." << endl;

    return 0;
}
