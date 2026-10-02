#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

bool findValue(TreeNode* root, int target) {
    // Base case: if root is null, target is not in the tree
    if (root == nullptr) {
        return false;
    }

    // If the current node matches the target, return true
    if (root->val == target) {
        return true;
    }

    // If target is less than current node's value, search the left subtree
    if (target < root->val) {
        return findValue(root->left, target);
    }
    // Otherwise, search the right subtree
    else {
        return findValue(root->right, target);
    }
}

int main() {
    // Example BST:
    //         8
    //       /   \
    //      3     10
    //     / \      \
    //    1   6      14
    TreeNode* root = new TreeNode(8);
    root->left = new TreeNode(3);
    root->right = new TreeNode(10);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(6);
    root->right->right = new TreeNode(14);

    int target = 6;

    if (findValue(root, target)) {
        cout << "Value " << target << " found in the BST." << endl;
    } else {
        cout << "Value " << target << " not found in the BST." << endl;
    }

    // Free allocated memory (for simplicity, manual deletion is omitted)
    return 0;
}
