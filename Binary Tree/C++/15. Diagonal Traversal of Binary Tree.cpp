#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// Definition of a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to perform diagonal traversal of the binary tree
vector<int> diagonalTraversal(Node* root) {
    vector<int> result;  // Vector to store the result of the diagonal traversal
    if (root == nullptr) return result;  // If the tree is empty, return an empty result
    
    queue<Node*> q;  // Queue to store nodes for level-order traversal
    q.push(root);  // Start with the root node

    while (!q.empty()) {
        Node* currentNode = q.front();  // Get the front node of the queue
        q.pop();  // Remove it from the queue

        // Process all nodes in the current diagonal (i.e., all nodes that are reachable via currentNode)
        while (currentNode) {
            result.push_back(currentNode->data);  // Add the current node's data to the result
            
            // If the current node has a left child, it belongs to the next diagonal, so we add it to the queue
            if (currentNode->left) {
                q.push(currentNode->left);
            }
            
            // Move to the right child for the same diagonal
            currentNode = currentNode->right;
        }
    }

    return result;  // Return the diagonal traversal result
}

// Helper function to print the diagonal traversal
void printDiagonalTraversal(Node* root) {
    vector<int> result = diagonalTraversal(root);  // Get the result from the diagonal traversal function
    for (int val : result) {
        cout << val << " ";  // Print each value in the result
    }
    cout << endl;  // End the output with a newline
}

// Main function to test the diagonal traversal
int main() {
    // Creating a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    root->left->right->left = new Node(8);
    root->left->right->right = new Node(9);

    // Print the diagonal traversal of the tree
    printDiagonalTraversal(root);  // Output: 1 2 3 4 5 6 7 8 9

    return 0;
}
