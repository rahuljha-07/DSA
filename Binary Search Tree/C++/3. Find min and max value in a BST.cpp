#include <iostream>
#include <stdexcept>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

// Function to find the minimum value in a BST
int findMin(Node* root) {
    if (root == nullptr) {
        throw invalid_argument("Tree is empty");
    }
    // Traverse left until you reach the leftmost node
    while (root->left != nullptr) {
        root = root->left;
    }
    return root->data;
}

// Function to find the maximum value in a BST
int findMax(Node* root) {
    if (root == nullptr) {
        throw invalid_argument("Tree is empty");
    }
    // Traverse right until you reach the rightmost node
    while (root->right != nullptr) {
        root = root->right;
    }
    return root->data;
}

int main() {
    // Example BST:
    //         8
    //       /   \
    //      3     10
    //     / \      \
    //    1   6      14
    Node* root = new Node(8);
    root->left = new Node(3);
    root->right = new Node(10);
    root->left->left = new Node(1);
    root->left->right = new Node(6);
    root->right->right = new Node(14);

    try {
        cout << "Minimum value in the BST: " << findMin(root) << endl;
        cout << "Maximum value in the BST: " << findMax(root) << endl;
    } catch (const invalid_argument& e) {
        cerr << e.what() << endl;
    }

    return 0;
}
