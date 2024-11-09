#include <vector>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Function to add left boundary nodes, excluding leaf nodes
    void addLeftBoundary(Node* root, vector<int>& boundaryNodes) {
        if (!root) return;
        if (root->left) {
            boundaryNodes.push_back(root->data);
            addLeftBoundary(root->left, boundaryNodes);
        } 
        else if (root->right) {
            boundaryNodes.push_back(root->data);
            addLeftBoundary(root->right, boundaryNodes);
        }
    }

    // Function to add all leaf nodes
    void addLeafNodes(Node* root, vector<int>& boundaryNodes) {
        if (!root) return;
        if (!root->left && !root->right) {
            boundaryNodes.push_back(root->data);
            return;
        }
        addLeafNodes(root->left, boundaryNodes);
        addLeafNodes(root->right, boundaryNodes);
    }

    // Function to add right boundary nodes in reverse order, excluding leaf nodes
    void addRightBoundary(Node* root, vector<int>& boundaryNodes) {
        if (!root) return;
        if (root->right) {
            addRightBoundary(root->right, boundaryNodes);
            boundaryNodes.push_back(root->data);
        } 
        else if (root->left) {
            addRightBoundary(root->left, boundaryNodes);
            boundaryNodes.push_back(root->data);
        }
    }

    // Main function to get the boundary traversal of the binary tree
    vector<int> printBoundary(Node* root) {
        vector<int> boundaryNodes;
        
        // If the tree is empty, return an empty vector
        if (!root) return boundaryNodes;

        // Add root node data if it's not a leaf
        boundaryNodes.push_back(root->data);

        // Add left boundary (excluding root and leaf nodes)
        addLeftBoundary(root->left, boundaryNodes);

        // Add leaf nodes
        addLeafNodes(root, boundaryNodes);

        // Add right boundary (excluding root and leaf nodes) in reverse order
        addRightBoundary(root->right, boundaryNodes);

        return boundaryNodes;
    }
};
