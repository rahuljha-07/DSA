#include <iostream>
using namespace std;

// Definition for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Recursive Inorder Traversal
void inorderRecursive(Node* root) {
    if (root == nullptr) {
        return;
    }

    inorderRecursive(root->left);   // Traverse left subtree
    cout << root->data << " ";       // Visit node
    inorderRecursive(root->right);  // Traverse right subtree
}

/ Iterative Inorder Traversal
void inorderIterative(Node* root) {
    stack<Node*> st;
    Node* current = root;

    while (current != nullptr || !st.empty()) {
        // Reach the leftmost node of the current node
        while (current != nullptr) {
            st.push(current);
            current = current->left;
        }

        // Current must be nullptr, so pop from the stack
        current = st.top();
        st.pop();

        // Visit the node
        cout << current->data << " ";

        // Visit the right subtree
        current = current->right;
    }
}

int main() {
    // Create a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Inorder traversal (Recursive): ";
    inorderRecursive(root);
    cout << endl;

    return 0;
}
