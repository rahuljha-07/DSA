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

// Global variable to store the result
int ans = -1;

// Helper function for finding the k-th largest element in BST
void findKthLargestHelper(Node* root, int k, int& count) {
    if (!root) return;  // Base case: if the node is null, return

    // Traverse the right subtree first (reverse in-order traversal)
    findKthLargestHelper(root->right, k, count);

    // Increment the count as we visit each node
    count++;

    // If count matches k, store the result in 'ans'
    if (count == k) {
        ans = root->data;
    }

    // Traverse the left subtree (still part of reverse in-order traversal)
    findKthLargestHelper(root->left, k, count);
}

// Public function to find the k-th largest element in the BST
int kthLargest(Node* root, int k) {
    int count = 0;  // Initialize the count to track how many nodes we've processed
    ans = -1;       // Initialize the answer as -1 (indicating not found yet)
    findKthLargestHelper(root, k, count);
    return ans;     // Return the k-th largest element (or -1 if not found)
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

    int k = 3;

    // Find the k-th largest element
    int kthLargestResult = kthLargest(root, k);
    cout << "The " << k << "-th largest element is: " << kthLargestResult << endl;

    return 0;
}
