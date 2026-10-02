#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

// Define the structure of a tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

unordered_map<string, int> subtreeMap; // Map to store subtree serializations and their counts

// Helper function to serialize subtrees and check for duplicates
string serializeSubtree(Node* root) {
    // Base case: if the node is null, return a unique symbol to represent it
    if (!root) return "$";

    // Serialize the left and right subtrees separately
    string leftString = serializeSubtree(root->left);
    string rightString = serializeSubtree(root->right);

    // Create the subtree representation
    string subtree = leftString + "," + to_string(root->data) + "," + rightString;

    // Increment the count of this serialized subtree in the map
    subtreeMap[subtree]++;

    return subtree;
}

// Main function to check if there is a duplicate subtree
bool hasDuplicateSubtree(Node* root) {
    subtreeMap.clear(); // Clear the map before starting

    // Serialize the entire tree
    serializeSubtree(root);

    // Check if any subtree appears more than once
    for (const auto& entry : subtreeMap) {
        if (entry.second >= 2) return true; // Duplicate subtree found
    }

    return false; // No duplicate subtrees
}

// Example usage
int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->right->left = new Node(2);
    root->right->left->left = new Node(4);
    root->right->right = new Node(4);

    cout << "Does the tree have a duplicate subtree? " << (hasDuplicateSubtree(root) ? "Yes" : "No") << endl;

    return 0;
}
