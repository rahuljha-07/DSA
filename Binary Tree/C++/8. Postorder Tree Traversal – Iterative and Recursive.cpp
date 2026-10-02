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

// Iterative Postorder Traversal (using one stack and a vector)
void postorderIterative(Node* root) {
    if (root == nullptr) {
        return;
    }

    stack<Node*> st1;
    vector<int> result; // To store the postorder traversal
    st1.push(root);

    while (!st1.empty()) {
        Node* current = st1.top();
        st1.pop();
        result.push_back(current->data); // Store the node data in the vector

        // Push left and right children to the stack
        if (current->left) {
            st1.push(current->left);
        }
        if (current->right) {
            st1.push(current->right);
        }
    }

    // Reverse the vector to get the correct postorder sequence
    reverse(result.begin(), result.end());

    // Print the postorder traversal
    for (int data : result) {
        cout << data << " ";
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
