#include <iostream>
#include <unordered_map>
using namespace std;

// Structure for a binary tree node
struct Node {
    int data;            // Value of the node
    Node* left;          // Pointer to the left child
    Node* right;         // Pointer to the right child
    Node(int val) {      // Constructor
        data = val;
        left = right = nullptr;
    }
};

// A hash map to store results of subproblems for memoization
unordered_map<Node*, int> dp;

// Function to calculate LIS for the binary tree
int LIS(Node* root) {
    // Base Case: If the node is NULL, LIS is 0
    if (root == nullptr)
        return 0;

    // If the result for this node is already computed, return it
    if (dp.find(root) != dp.end())
        return dp[root];

    // Case 1: Include the current node in LIS
    int include = 1; // Include the current node
    if (root->left) {
        // Add LIS of left-left and left-right (grandchildren)
        include += LIS(root->left->left) + LIS(root->left->right);
    }
    if (root->right) {
        // Add LIS of right-left and right-right (grandchildren)
        include += LIS(root->right->left) + LIS(root->right->right);
    }

    // Case 2: Exclude the current node from LIS
    // Add LIS of immediate children (left and right)
    int exclude = LIS(root->left) + LIS(root->right);

    // Store the maximum of include and exclude in dp
    dp[root] = max(include, exclude);

    // Return the computed value
    return dp[root];
}

// Helper function to free the dynamically allocated memory
void deleteTree(Node* root) {
    if (root == nullptr)
        return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

// Main function to test the implementation
int main() {
    // Constructing the tree:
    //                 10
    //                /   \
    //              20      30
    //            /    \        \
    //          40     50       60
    //                 /  \
    //               70    80
    Node* root = new Node(10);
    root->left = new Node(20);
    root->right = new Node(30);
    root->left->left = new Node(40);
    root->left->right = new Node(50);
    root->right->right = new Node(60);
    root->left->right->left = new Node(70);
    root->left->right->right = new Node(80);

    // Find the Largest Independent Set (LIS)
    cout << "Size of the Largest Independent Set: " << LIS(root) << endl;

    // Free the allocated memory
    deleteTree(root);
    return 0;
}
