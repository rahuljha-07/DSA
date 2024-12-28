#include <iostream>
#include <vector>
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

// Helper function to print a path
void printPath(const vector<int>& path) {
    for (int val : path) {
        cout << val << " ";
    }
    cout << endl;
}

// Recursive DFS function to find paths with sum = k
void findKSumPaths(Node* root, vector<int>& path, int k, int currentSum) {
    if (!root) return;

    // Add the current node to the path and update the sum
    path.push_back(root->data);
    currentSum += root->data;

    // Check if the sum of the current path equals k
    if (currentSum == k) {
        printPath(path);  // Print the path
    }

    // Explore left and right subtrees
    findKSumPaths(root->left, path, k, currentSum);
    findKSumPaths(root->right, path, k, currentSum);

    // Backtrack: remove the last node from the path
    path.pop_back();
}

// Function to start the process for all nodes in the tree
void printAllKSumPaths(Node* root, int k) {
    if (!root) return;

    // Temporary vector to store the current path
    vector<int> path;

    // Start the DFS traversal from the current node
    findKSumPaths(root, path, k, 0);

    // Recursively check for paths starting at the left and right subtrees
    printAllKSumPaths(root->left, k);
    printAllKSumPaths(root->right, k);
}

// Wrapper function to initialize parameters and call the core logic
void printPathsWithSum(Node* root, int k) {
    cout << "Paths with sum " << k << " are:" << endl;
    printAllKSumPaths(root, k);
}

int main() {
    // Example binary tree:
    //             1
    //          /     \
    //        3        -1
    //      /   \     /   \
    //    2     1   4       5
    //        /   /    \         \
    //     1   1          2          6

    Node* root = new Node(1);
    root->left = new Node(3);
    root->right = new Node(-1);
    root->left->left = new Node(2);
    root->left->right = new Node(1);
    root->right->left = new Node(4);
    root->right->right = new Node(5);
    root->left->right->left = new Node(1);
    root->right->left->left = new Node(1);
    root->right->right->right = new Node(2);
    root->right->right->right->right = new Node(6);

    int k = 5;

    // Call the wrapper function
    printPathsWithSum(root, k);

    return 0;
}
