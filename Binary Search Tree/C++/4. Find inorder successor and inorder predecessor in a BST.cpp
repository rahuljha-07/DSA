#include <iostream>

using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;

    Node(int value) : key(value), left(nullptr), right(nullptr) {}
};

/// Function to find predecessor and successor
void findPreSuc(Node* root, Node*& pre, Node*& suc, int key) {
    if (!root) return;

    // Traverse left subtree to find potential predecessor
    findPreSuc(root->left, pre, suc, key);
    
    // Check if the current node can be a predecessor or successor
    if (root->key < key) {
        pre = root;  // Update predecessor
    } else if (root->key > key && !suc) {
        suc = root;  // Update successor if it's the first larger node found
    }

    // Traverse right subtree to find potential successor
    findPreSuc(root->right, pre, suc, key);
}


// Helper function to insert a node in BST
Node* insert(Node* root, int key) {
    if (!root) return new Node(key);

    if (key < root->key) {
        root->left = insert(root->left, key);
    } else if (key > root->key) {
        root->right = insert(root->right, key);
    }
    return root;
}

int main() {
    // Example BST
    Node* root = nullptr;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    int key = 65;
    Node* pre = nullptr;
    Node* suc = nullptr;

    findPreSuc(root, pre, suc, key);

    if (pre) {
        cout << "Predecessor is " << pre->key << endl;
    } else {
        cout << "No Predecessor" << endl;
    }

    if (suc) {
        cout << "Successor is " << suc->key << endl;
    } else {
        cout << "No Successor" << endl;
    }

    return 0;
}
