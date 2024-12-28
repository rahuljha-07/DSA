#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Function to balance an unbalanced BST
    Node* balanceBST(Node* root) {
        vector<int> sortedNodes;
        inorderTraversal(root, sortedNodes);  // Step 1: Collect nodes in sorted order
        return buildBalancedBST(sortedNodes, 0, sortedNodes.size() - 1);  // Step 2: Build balanced BST
    }

private:
    // Helper function to perform inorder traversal and store nodes in a sorted list
    void inorderTraversal(Node* root, vector<int>& sortedNodes) {
        if (!root) return;
        inorderTraversal(root->left, sortedNodes);
        sortedNodes.push_back(root->data);
        inorderTraversal(root->right, sortedNodes);
    }

    // Helper function to construct a balanced BST from a sorted list of nodes
    Node* buildBalancedBST(vector<int>& sortedNodes, int start, int end) {
        if (start > end) return nullptr;

        // Choose the middle element as the root
        int mid = (start + end) / 2;
        Node* root = new Node(sortedNodes[mid]);

        // Recursively build the left and right subtrees
        root->left = buildBalancedBST(sortedNodes, start, mid - 1);
        root->right = buildBalancedBST(sortedNodes, mid + 1, end);

        return root;
    }
};

// Helper function to print the inorder traversal of the tree (for verification)
void inorderPrint(Node* root) {
    if (!root) return;
    inorderPrint(root->left);
    cout << root->data << " ";
    inorderPrint(root->right);
}

int main() {
    // Example of an unbalanced BST
    Node* root = new Node(10);
    root->left = new Node(5);
    root->left->left = new Node(1);
    root->right = new Node(15);
    root->right->right = new Node(20);

    Solution solution;
    Node* balancedRoot = solution.balanceBST(root);

    // Print the inorder traversal of the balanced BST (should be sorted)
    cout << "Inorder Traversal of Balanced BST: ";
    inorderPrint(balancedRoot);
    cout << endl;

    return 0;
}
