#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

vector<int> values;  // Stores the last two visited node values during traversal
int isBSTFlag;       // Flag to store the result (1 if BST, 0 if not)

void inOrderTraverse(Node* root) {
    if (root==nullptr || isBSTFlag == 0) return;  // Base case and early exit if tree is not BST

    // Traverse the left subtree
    inOrderTraverse(root->left);

    // Check current node
    if (values.size() < 2) {
        values.push_back(root->data);  // Add the first two values
    } else {
        // Check if the values are in increasing order
        if (values[0] < values[1]) { 
            values[0] = values[1];       // Shift values to the left
            values[1] = root->data;      // Update with the current node's data
        } else {
            isBSTFlag = 0;               // Not a BST
            return;
        }
    }

    // Traverse the right subtree
    inOrderTraverse(root->right);
}

bool isBST(Node* root) {
    isBSTFlag = 1;       // Assume tree is a BST initially
    values.clear();      // Clear values before starting
    inOrderTraverse(root);
    return isBSTFlag;
}

// Helper function to insert nodes in the BST
Node* insert(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->data) root->left = insert(root->left, key);
    else if (key > root->data) root->right = insert(root->right, key);
    return root;
}

int main() {
    Node* root = new Node(4);
    root->left = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(1);
    root->left->right = new Node(3);

    if (isBST(root)) {
        cout << "The tree is a Binary Search Tree (BST)." << endl;
    } else {
        cout << "The tree is NOT a Binary Search Tree (BST)." << endl;
    }

    return 0;
}
