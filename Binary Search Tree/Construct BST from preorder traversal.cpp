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
    // Function to construct BST from the given preorder traversal array
    Node* bstFromPreorder(vector<int>& preorder) {
        return helper(preorder, 0, preorder.size());  // Start with the entire range
    }

private:
    // Helper function to recursively build the BST
    Node* helper(vector<int>& preorder, int rootIndex, int rightLimit) {
        // Base case: if we've reached the end of the array, return null
        if (rootIndex >= rightLimit) {
            return nullptr;
        }

        // Get the value of the current root node from the preorder array
        int value = preorder[rootIndex];
        Node* root = new Node(value);

        // Find the right child index (first value greater than current node value)
        int i = rootIndex + 1;
        while (i < preorder.size() && preorder[i] < value) {
            i++;  // Move to the right if the value is smaller than the current root
        }

        // Recursively build the left and right subtrees
        root->left = helper(preorder, rootIndex + 1, i);  // Left subtree: nodes smaller than root
        root->right = helper(preorder, i, rightLimit);    // Right subtree: nodes greater than root

        return root;  // Return the root node
    }
};

// Helper function to print the inorder traversal of the tree (for verification)
void inorderTraversal(Node* root) {
    if (!root) return;
    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}

int main() {
    // Example preorder traversal
    vector<int> preorder = {40, 30, 35, 80, 100};

    // Construct BST from the given preorder traversal
    Solution solution;
    Node* root = solution.bstFromPreorder(preorder);

    // Print the inorder traversal of the constructed BST (should be sorted)
    cout << "Inorder Traversal of the Constructed BST: ";
    inorderTraversal(root);
    cout << endl;

    return 0;
}
