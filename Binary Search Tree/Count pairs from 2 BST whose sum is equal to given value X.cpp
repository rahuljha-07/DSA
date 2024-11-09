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
    // Function to count pairs from two BSTs whose sum is equal to given value X
    int countPairs(Node* root1, Node* root2, int X) {
        // Step 1: Get sorted arrays from both BSTs
        vector<int> bst1Elements, bst2Elements;
        inorderTraversal(root1, bst1Elements);
        inorderTraversal(root2, bst2Elements);

        // Step 2: Use two-pointer technique to count pairs with sum X
        int count = 0;
        int i = 0;  // Pointer for bst1Elements (start of first array)
        int j = bst2Elements.size() - 1;  // Pointer for bst2Elements (end of second array)

        while (i < bst1Elements.size() && j >= 0) {
            int sum = bst1Elements[i] + bst2Elements[j];
            if (sum == X) {
                count++;
                i++;
                j--;
            } else if (sum < X) {
                i++;
            } else {
                j--;
            }
        }

        return count;
    }

private:
    // Helper function to perform inorder traversal and store nodes in a sorted list
    void inorderTraversal(Node* root, vector<int>& elements) {
        if (!root) return;
        inorderTraversal(root->left, elements);
        elements.push_back(root->data);
        inorderTraversal(root->right, elements);
    }
};

// Helper function to create a simple BST (for testing)
Node* insertBST(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->data) root->left = insertBST(root->left, key);
    else root->right = insertBST(root->right, key);
    return root;
}

int main() {
    // Construct two sample BSTs
    Node* root1 = nullptr;
    root1 = insertBST(root1, 5);
    insertBST(root1, 3);
    insertBST(root1, 7);
    insertBST(root1, 2);
    insertBST(root1, 4);

    Node* root2 = nullptr;
    root2 = insertBST(root2, 10);
    insertBST(root2, 6);
    insertBST(root2, 15);
    insertBST(root2, 3);
    insertBST(root2, 8);

    int targetSum = 9;

    Solution solution;
    int pairCount = solution.countPairs(root1, root2, targetSum);

    cout << "Number of pairs with sum " << targetSum << ": " << pairCount << endl;

    return 0;
}
