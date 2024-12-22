#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Function to check if all levels of two trees are anagrams
bool areAnagrams(TreeNode* root1, TreeNode* root2) {
    if (!root1 && !root2) return true;   // Both trees are empty
    if (!root1 || !root2) return false;  // Only one of the trees is empty

    queue<TreeNode*> q1, q2;
    q1.push(root1);
    q2.push(root2);

    // Perform level-order traversal for both trees simultaneously
    while (!q1.empty() && !q2.empty()) {
        int size1 = q1.size();
        int size2 = q2.size();

        // If the number of nodes at current level are different
        if (size1 != size2) return false;

        vector<int> level1, level2;

        // Process all nodes at the current level for tree 1
        for (int i = 0; i < size1; i++) {
            TreeNode* node1 = q1.front();
            q1.pop();
            level1.push_back(node1->val);

            if (node1->left) q1.push(node1->left);
            if (node1->right) q1.push(node1->right);
        }

        // Process all nodes at the current level for tree 2
        for (int i = 0; i < size2; i++) {
            TreeNode* node2 = q2.front();
            q2.pop();
            level2.push_back(node2->val);

            if (node2->left) q2.push(node2->left);
            if (node2->right) q2.push(node2->right);
        }

        // Sort and compare both levels
        sort(level1.begin(), level1.end());
        sort(level2.begin(), level2.end());
        
        if (level1 != level2) return false;
    }

    // Check if both queues are empty (same structure)
    return q1.empty() && q2.empty();
}

// Helper function to create a new tree node
TreeNode* newNode(int data) {
    return new TreeNode(data);
}

// Main function to test the anagram level check
int main() {
    /* Construct the following trees
        Tree 1:         Tree 2:
           1               1
         /   \           /   \
        2     3         3     2
       /                 \
      4                   4
    */

    TreeNode* root1 = newNode(1);
    root1->left = newNode(2);
    root1->right = newNode(3);
    root1->left->left = newNode(4);

    TreeNode* root2 = newNode(1);
    root2->left = newNode(3);
    root2->right = newNode(2);
    root2->left->right = newNode(4);

    if (areAnagrams(root1, root2))
        cout << "All levels of both trees are anagrams.\n";
    else
        cout << "All levels of both trees are not anagrams.\n";

    return 0;
}
