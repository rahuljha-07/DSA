#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

// Helper function to find the maximum value in the left subtree
Node* findMax(Node* root) {
    while (root->right != nullptr) {
        root = root->right;
    }
    return root;
}

Node* deleteNode(Node* root, int key) {
    // Base case: if the tree is empty, return nullptr
    if (root == nullptr) {
        return nullptr;
    }

    // Traverse the tree to find the node to delete
    if (key > root->data) {
        root->right = deleteNode(root->right, key);  // Search in the right subtree
    } 
    else if (key < root->data) {
        root->left = deleteNode(root->left, key);    // Search in the left subtree
    } 
    else {
        // Node to delete is found

        // Case 1: No children (leaf node)
        if (root->left == nullptr && root->right == nullptr) {
            delete root;
            return nullptr;
        }
        
        // Case 2: Node has only right child
        else if (root->left == nullptr) {
            Node* temp = root->right;
            delete root;
            return temp;
        }
        
        // Case 3: Node has only left child
        else if (root->right == nullptr) {
            Node* temp = root->left;
            delete root;
            return temp;
        }

        // Case 4: Node has two children
        else {
            // Find the maximum value in the left subtree
            Node* maxNode = findMax(root->left);
            root->data = maxNode->data;  // Replace root's data with max value in left subtree
            root->left = deleteNode(root->left, maxNode->data);  // Delete the duplicate node
        }
    }

    // Return the (possibly modified) root pointer
    return root;
}

// Function to perform an in-order traversal for testing
void inOrderTraversal(Node* root) {
    if (root != nullptr) {
        inOrderTraversal(root->left);
        cout << root->data << " ";
        inOrderTraversal(root->right);
    }
}

int main() {
    // Example BST:
    //         8
    //       /   \
    //      3     10
    //     / \      \
    //    1   6      14
    Node* root = new Node(8);
    root->left = new Node(3);
    root->right = new Node(10);
    root->left->left = new Node(1);
    root->left->right = new Node(6);
    root->right->right = new Node(14);

    int keyToDelete = 3;
    root = deleteNode(root, keyToDelete);

    cout << "In-order traversal after deletion: ";
    inOrderTraversal(root);
    cout << endl;

    return 0;
}
