#include <iostream>
#include <climits>
using namespace std;

// Definition for a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to calculate the diameter of a binary tree
// The diameter of a tree is the number of nodes on the longest path between two leaves.
class Solution {
private:
    int maxDiameter;  // This will hold the maximum diameter found during recursion

public:
    // Helper function to calculate the height of the tree and update the diameter
    int calculateHeight(Node* root) {
        if (!root) return 0;  // If the node is null, return height as 0
        
        // Recursively calculate the height of the left and right subtrees
        int leftHeight = calculateHeight(root->left);
        int rightHeight = calculateHeight(root->right);

        // The height of the current node is the maximum of the left and right subtrees plus 1
        int currentHeight = max(leftHeight, rightHeight) + 1;

        // Calculate the diameter at the current node (sum of left and right heights)
        int currentDiameter = leftHeight + rightHeight + 1;

        // Update the maximum diameter if the current diameter is larger
        maxDiameter = max(maxDiameter, currentDiameter);

        return currentHeight;  // Return the height of the current node
    }

    // Main function to return the diameter of the binary tree
    int diameter(Node* root) {
        maxDiameter = INT_MIN;  // Initialize the maximum diameter to a very small value
        calculateHeight(root);  // Start the recursive calculation
        return maxDiameter;  // Return the maximum diameter found
    }
};

int main() {
    // Create a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    Solution solution;
    cout << "Diameter of the tree: " << solution.diameter(root) << endl;

    return 0;
}
