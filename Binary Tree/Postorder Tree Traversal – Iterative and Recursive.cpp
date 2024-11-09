#include <iostream>
using namespace std;

// Definition for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Recursive Postorder Traversal (Left, Right, Root)
void postorderRecursive(Node* root) {
    if (root == nullptr) {
        return;
    }

    // Recursively visit left subtree
    postorderRecursive(root->left);

    // Recursively visit right subtree
    postorderRecursive(root->right);

    // Visit the root node
    cout << root->data << " ";
}

// Iterative Postorder Traversal (using two stacks)
void postorderIterative(Node* root) {
    if (root == nullptr) {
        return;
    }

    stack<Node*> st1, st2;
    st1.push(root);

    while (!st1.empty()) {
        Node* current = st1.top();
        st1.pop();
        st2.push(current);  // Push to second stack

        // Push left and right children to the first stack
        if (current->left) {
            st1.push(current->left);
        }
        if (current->right) {
            st1.push(current->right);
        }
    }

    // Now pop all elements from the second stack and print them
    while (!st2.empty()) {
        cout << st2.top()->data << " ";
        st2.pop();
    }
}


int main() {
    // Create a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Postorder traversal (Recursive): ";
    postorderRecursive(root);
    cout << endl;

    return 0;
}
