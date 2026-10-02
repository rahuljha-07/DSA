#include <iostream>
using namespace std;

// Structure for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Helper function to find the LCA of two nodes
Node* findLCA(Node* root, int n1, int n2) {
    if (!root) return nullptr;
    
    if (root->data == n1 || root->data == n2) return root;
    
    Node* leftLCA = findLCA(root->left, n1, n2);
    Node* rightLCA = findLCA(root->right, n1, n2);

    if (leftLCA && rightLCA) return root;
    
    return leftLCA ? leftLCA : rightLCA;
}

// Function to find the distance from the root to a given node
int findDistanceFromRoot(Node* root, int target, int distance) {
    if (!root) return -1;  // If the root is NULL, return -1
    
    // If the current node is the target, return the current distance
    if (root->data == target) return distance;
    
    // Search in the left subtree
    int leftDistance = findDistanceFromRoot(root->left, target, distance + 1);
    
    // If the target is found in the left subtree, return the left distance
    if (leftDistance != -1) {
        return leftDistance;
    }

    // Search in the right subtree
    int rightDistance = findDistanceFromRoot(root->right, target, distance + 1);
    
    // If the target is found in the right subtree, return the right distance
    if (rightDistance != -1) {
        return rightDistance;
    }

    // If the target is not found in either subtree, return -1
    return -1;
}

// Function to find the minimum distance between two nodes
int findMinDistance(Node* root, int a, int b) {
    // Step 1: Find the LCA of the two nodes
    Node* lca = findLCA(root, a, b);
    if (!lca) return -1; // If LCA is not found, nodes are not in the same tree

    // Step 2: Calculate the distance from the LCA to each of the two nodes
    int distanceA = findDistanceFromRoot(lca, a, 0);
    int distanceB = findDistanceFromRoot(lca, b, 0);

    // Step 3: The minimum distance is the sum of the distances from LCA to each node
    return distanceA + distanceB;
}

int main() {
    // Constructing the binary tree
    Node* root = new Node(11);
    root->left = new Node(22);
    root->right = new Node(33);
    root->left->left = new Node(44);
    root->left->right = new Node(55);
    root->right->left = new Node(66);
    root->right->right = new Node(77);

    int a = 77, b = 22;
    int minDistance = findMinDistance(root, a, b);

    cout << "Minimum distance between nodes " << a << " and " << b << " is " << minDistance << endl;

    return 0;
}
