#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Definition for a Binary Tree Node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

// Helper function to perform inorder traversal and store the elements in a vector
void inorderTraversal(Node* root, vector<int>& elements) {
    if (root == nullptr) return;

    inorderTraversal(root->left, elements);  // Traverse left subtree
    elements.push_back(root->data);           // Visit node
    inorderTraversal(root->right, elements); // Traverse right subtree
}

// Helper function to perform level order traversal and assign elements from the sorted array
void convertBSTToMinHeap(Node* root, vector<int>& elements, int& idx) {
    if (root == nullptr) return;

    // Assign the current node value from the sorted list
    root->data = elements[idx++];
    
    // Perform level order traversal for left and right children
    if (root->left) convertBSTToMinHeap(root->left, elements, idx);
    if (root->right) convertBSTToMinHeap(root->right, elements, idx);
}

// Main function to convert BST to Min Heap
Node* convertToMinHeap(Node* root) {
    // Step 1: Perform inorder traversal and store elements in a sorted list
    vector<int> elements;
    inorderTraversal(root, elements);

    // Step 2: Reassign elements from sorted list to the BST nodes using level-order traversal
    int idx = 0;
    convertBSTToMinHeap(root, elements, idx);
    
    return root;
}

// Function to print the tree in level order (for testing)
void levelOrderTraversal(Node* root) {
    if (!root) return;
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* current = q.front();
        q.pop();
        cout << current->data << " ";
        
        if (current->left) q.push(current->left);
        if (current->right) q.push(current->right);
    }
    cout << endl;
}

int main() {
    // Create a sample BST (complete binary tree)
    Node* root = new Node(10);
    root->left = new Node(5);
    root->right = new Node(20);
    root->left->left = new Node(3);
    root->left->right = new Node(7);
    root->right->left = new Node(15);
    root->right->right = new Node(25);
    
    cout << "Original BST (level order): ";
    levelOrderTraversal(root);

    // Convert BST to Min Heap
    root = convertToMinHeap(root);
    
    cout << "Converted Min Heap (level order): ";
    levelOrderTraversal(root);
    
    return 0;
}
// for max heap run array loop in reverse order