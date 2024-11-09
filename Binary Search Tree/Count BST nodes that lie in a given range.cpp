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

// Helper function to perform inorder traversal and count nodes within the given range [l, h]
void inorder(Node* root, int l, int h, int& count) {
    // Base case: if the current node is null, return
    if (!root) return;
    
    // Traverse the left subtree
    inorder(root->left, l, h, count);
    
    // Check if the current node's value is within the range [l, h]
    if (l <= root->data && root->data <= h) {
        count++;  // Increment the count if the value is within the range
    }
    
    // Traverse the right subtree
    inorder(root->right, l, h, count);
}

// Function to count nodes in the BST whose values are within the range [l, h]
int getCount(Node* root, int l, int h) {
    int count = 0;  // Initialize count to 0
    inorder(root, l, h, count);  // Call inorder traversal to count nodes in the range
    return count;  // Return the total count
}

int main() {
    // Example BST:
    //         5
    //      /     \
    //    3         8
    //   /  \      /   \
    //  2    4    6     9

    Node* root = new Node(5);
    root->left = new Node(3);
    root->right = new Node(8);
    root->left->left = new Node(2);
    root->left->right = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(9);

    int l = 4, h = 8;
    int count = getCount(root, l, h);
    cout << "The number of nodes in the range [" << l << ", " << h << "] is: " << count << endl;

    return 0;
}
