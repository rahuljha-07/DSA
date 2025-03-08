#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Definition of the Node structure
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Function to collect the left boundary (excluding leaf nodes)
void getLeftBoundary(Node* root, vector<int>& boundary) {
    Node* curr = root;
    while (curr) {
        // Add to boundary only if it's not a leaf node
        if (curr->left || curr->right)
            boundary.push_back(curr->data);
        
        // Move to the left child if exists, else move to right child
        if (curr->left)
            curr = curr->left;
        else
            curr = curr->right;
    }
}

// Function to collect leaf nodes (in-order traversal)
void getLeafNodes(Node* root, vector<int>& boundary) {
    if (!root) return;

    // Traverse left subtree
    getLeafNodes(root->left, boundary);

    // Store only leaf nodes
    if (!root->left && !root->right)
        boundary.push_back(root->data);

    // Traverse right subtree
    getLeafNodes(root->right, boundary);
}

// Function to collect the right boundary (excluding leaf nodes, in reverse order)
void getRightBoundary(Node* root, vector<int>& boundary) {
    vector<int> temp; // Temporary vector to store right boundary

    Node* curr = root;
    while (curr) {
        // Add to temp only if it's not a leaf node
        if (curr->left || curr->right)
            temp.push_back(curr->data);
        
        // Move to the right child if exists, else move to left child
        if (curr->right)
            curr = curr->right;
        else
            curr = curr->left;
    }

    // Add right boundary in reverse order
    for (int i = temp.size() - 1; i >= 0; i--)
        boundary.push_back(temp[i]);
}

// Main function to get the boundary traversal
vector<int> boundaryTraversal(Node* root) {
    vector<int> boundary;

    if (!root) return boundary;

    // Step 1: Add the root node
    boundary.push_back(root->data);

    // Step 2: Collect left boundary (excluding root and leaf nodes)
    if (root->left)
        getLeftBoundary(root->left, boundary);

    // Step 3: Collect all leaf nodes (in-order traversal)
    getLeafNodes(root, boundary);

    // Step 4: Collect right boundary (excluding root and leaf nodes, reversed)
    if (root->right)
        getRightBoundary(root->right, boundary);

    return boundary;
}

// Function to print the boundary traversal
void printBoundary(vector<int> boundary) {
    for (int val : boundary)
        cout << val << " ";
    cout << endl;
}

// Driver Code
int main() {
    /*
          1
        /   \
       2     3
      / \   / \
     4   5 6  7
        / \
       8   9
    */
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->left->right->left = new Node(8);
    root->left->right->right = new Node(9);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    vector<int> boundary = boundaryTraversal(root);
    printBoundary(boundary);

    return 0;
}
