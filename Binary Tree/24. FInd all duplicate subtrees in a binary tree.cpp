#include <unordered_map>
#include <vector>
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
vector<Node*> duplicateRoots; // Vector to store roots of duplicate subtrees

// Helper function to serialize subtrees and check for duplicates
string findDuplicateSubtreesUtil(Node* root) {
    if (!root) return "#"; // Use "#" to represent null nodes to avoid ambiguity

    // Serialize the current subtree as a string
    string subtree = to_string(root->data) + "," + 
                     findDuplicateSubtreesUtil(root->left) + "," + 
                     findDuplicateSubtreesUtil(root->right);

    // If this subtree has already appeared once, add its root to duplicateRoots
    if (subtreeMap[subtree] == 1) {
        duplicateRoots.push_back(root);
    }

    // Increment the count of this serialized subtree
    subtreeMap[subtree]++;

    return subtree;
}

// Main function to find all duplicate subtrees
vector<Node*> findDuplicateSubtrees(Node* root) {
    subtreeMap.clear(); // Clear the map before starting
    duplicateRoots.clear(); // Clear the duplicates list before starting

    findDuplicateSubtreesUtil(root); // Populate the map and collect duplicate roots

    return duplicateRoots; // Return all root nodes of duplicate subtrees
}

// Helper function to print a subtree rooted at the given node
void printSubtree(Node* root) {
    if (!root) return;
    cout << root->data << " ";
    printSubtree(root->left);
    printSubtree(root->right);
}

// Example usage
int main() {
    // Constructing the tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->right->left = new Node(2);
    root->right->left->left = new Node(4);
    root->right->right = new Node(4);

    // Find and print all duplicate subtrees
    vector<Node*> duplicates = findDuplicateSubtrees(root);
    cout << "Duplicate Subtrees:\n";
for (Node* duplicateRoot : duplicates) {
        printSubtree(duplicateRoot); // Print the subtree
        cout << endl;
    }

    return 0;
}
