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
    // Function to merge two balanced BSTs
    Node* mergeTrees(Node* root1, Node* root2) {
        // Step 1: Get the sorted arrays from both BSTs
        vector<int> tree1Nodes, tree2Nodes;
        inorderTraversal(root1, tree1Nodes);
        inorderTraversal(root2, tree2Nodes);

        // Step 2: Merge the two sorted arrays
        vector<int> mergedNodes = mergeSortedArrays(tree1Nodes, tree2Nodes);

        // Step 3: Build a balanced BST from the merged sorted array
        return buildBalancedBST(mergedNodes, 0, mergedNodes.size() - 1);
    }

private:
    // Helper function to perform inorder traversal and store nodes in a sorted list
    void inorderTraversal(Node* root, vector<int>& sortedNodes) {
        if (!root) return;
        inorderTraversal(root->left, sortedNodes);
        sortedNodes.push_back(root->data);
        inorderTraversal(root->right, sortedNodes);
    }

    // Helper function to merge two sorted arrays
    vector<int> mergeSortedArrays(const vector<int>& arr1, const vector<int>& arr2) {
        vector<int> merged;
        int i = 0, j = 0;
        while (i < arr1.size() && j < arr2.size()) {
            if (arr1[i] < arr2[j]) {
                merged.push_back(arr1[i++]);
            } else {
                merged.push_back(arr2[j++]);
            }
        }
        while (i < arr1.size()) merged.push_back(arr1[i++]);
        while (j < arr2.size()) merged.push_back(arr2[j++]);
        return merged;
    }

    // Helper function to build a balanced BST from a sorted list of nodes
    Node* buildBalancedBST(const vector<int>& sortedNodes, int start, int end) {
        if (start > end) return nullptr;

        int mid = (start + end) / 2;
        Node* root = new Node(sortedNodes[mid]);

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
    // Example trees
    Node* root1 = new Node(3);
    root1->left = new Node(1);
    root1->right = new Node(5);

    Node* root2 = new Node(4);
    root2->left = new Node(2);
    root2->right = new Node(6);

    Solution solution;
    Node* mergedRoot = solution.mergeTrees(root1, root2);

    // Print the inorder traversal of the merged balanced BST (should be sorted)
    cout << "Inorder Traversal of Merged Balanced BST: ";
    inorderPrint(mergedRoot);
    cout << endl;

    return 0;
}
