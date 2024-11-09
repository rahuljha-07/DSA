#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node* next; // Pointer to store the in-order successor

    Node(int value) : data(value), left(nullptr), right(nullptr), next(nullptr) {}
};

Node* prevNode = nullptr; // Global variable to keep track of the previously visited node

// Function to populate the next pointer (in-order successor) for all nodes
void populateInorderSuccessor(Node* currentNode) {
    // Base case: If current node is null, return
    if (!currentNode) return;

    // Traverse the left subtree first (in-order)
    populateInorderSuccessor(currentNode->left);

    // If prevNode is not null, set the next pointer of prevNode to currentNode
    if (prevNode != nullptr) {
        prevNode->next = currentNode;
    }

    // Update prevNode to current node
    prevNode = currentNode;

    // Traverse the right subtree
    populateInorderSuccessor(currentNode->right);
}

// Helper function to insert nodes into the binary search tree
Node* insert(Node* root, int key) {
    if (!root) return new Node(key);  // If the tree is empty, create a new node

    if (key < root->data) {
        root->left = insert(root->left, key);  // Insert into the left subtree
    } else if (key > root->data) {
        root->right = insert(root->right, key);  // Insert into the right subtree
    }

    return root;
}

// Helper function to print the in-order successor of each node
void printInorderSuccessors(Node* root) {
    if (root) {
        // Print the left subtree first
        printInorderSuccessors(root->left);

        // Print the in-order successor of the current node
        if (root->next) {
            cout << "In-order successor of " << root->data << " is " << root->next->data << endl;
        } else {
            cout << "In-order successor of " << root->data << " is NULL" << endl;
        }

        // Print the right subtree
        printInorderSuccessors(root->right);
    }
}

int main() {
    Node* root = nullptr;
    // Create the BST by inserting nodes
    root = insert(root, 4);
    insert(root, 2);
    insert(root, 5);
    insert(root, 1);
    insert(root, 3);

    // Populate the in-order successor for all nodes
    populateInorderSuccessor(root);

    // Print the in-order successors for each node
    printInorderSuccessors(root);

    return 0;
}
