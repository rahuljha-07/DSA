#include <iostream>
using namespace std;

// Definition for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Recursive Preorder Traversal
void preorderRecursive(Node* root) {
    if (root == nullptr) {
        return;
    }

    cout << root->data << " ";         // Visit the node
    preorderRecursive(root->left);     // Traverse left subtree
    preorderRecursive(root->right);    // Traverse right subtree
}

// Iterative Preorder Traversal
void preorderIterative(Node* root) {
    if (root == nullptr) {
        return;
    }

    stack<Node*> st;
    st.push(root);  // Push the root to the stack

    while (!st.empty()) {
        Node* current = st.top();  // Get the top node from the stack
        st.pop();  // Pop the node from the stack

        cout << current->data << " ";  // Visit the node

        // Push the right child first so that the left child is processed first
        if (current->right) {
            st.push(current->right);
        }

        // Push the left child to the stack
        if (current->left) {
            st.push(current->left);
        }
    }
}

int main() {
    // Create a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Preorder traversal (Recursive): ";
    preorderRecursive(root);
    cout << endl;

    return 0;
}
