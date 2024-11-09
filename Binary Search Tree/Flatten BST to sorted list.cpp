#include <iostream>
using namespace std;

// Structure for a binary search tree (BST) node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Helper function to perform in-order traversal and flatten the BST
void inorder(Node* root, Node*& prev, Node*& head) {
    // Base case: if the root is null, return
    if (!root) return;

    // Recursively traverse the left subtree
    inorder(root->left, prev, head);

    // If prev is not null, update the pointers to flatten the tree
    if (prev) {
        prev->right = root;  // Set the right of prev to point to the current node
        prev->left = nullptr;  // Set the left of prev to nullptr as it is now a linked list
    } else {
        // If prev is null, this means it's the first node, so set it as the head
        head = root;
    }
    
    // Move prev pointer to the current node
    prev = root;

    // Recursively traverse the right subtree
    inorder(root->right, prev, head);
}

// Function to flatten the BST into a sorted linked list
Node* flattenBST(Node* root) {
    Node* prev = nullptr;  // Initialize prev pointer as null
    Node* head = nullptr;  // Initialize head pointer as null
    inorder(root, prev, head);   // Perform in-order traversal to flatten the BST
    return head;           // Return the head of the flattened list
}

// Helper function to print the linked list
void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->right;
    }
    cout << endl;
}

int main() {
    // Example BST:
    //         5
    //      /     \
    //    3         8
    //   /  \      /   \
    //  2    4    6     9

    Node* root = new Node(5);
    root->left = new Node(3);
    root->right = new Node(8);
    root->left->left = new Node(2);
    root->left->right = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(9);

    // Flatten the BST into a sorted linked list
    Node* flattenedHead = flattenBST(root);

    // Print the flattened list
    printList(flattenedHead);

    return 0;
}
