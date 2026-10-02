#include <iostream>
using namespace std;

// Definition of a binary tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Recursive function to check if two trees are isomorphic
bool isIsomorphic(Node* T1, Node* T2) {
    // Base cases
    if (!T1 && !T2) return true;      // Both nodes are null
    if (!T1 || !T2) return false;     // One node is null, the other is not
    if (T1->data != T2->data) return false; // Data mismatch

    // Check isomorphism without flipping or with flipping children
    bool withoutFlip = isIsomorphic(T1->left, T2->left) && isIsomorphic(T1->right, T2->right);
    bool withFlip = isIsomorphic(T1->left, T2->right) && isIsomorphic(T1->right, T2->left);

    // Return true if either configuration is isomorphic
    return withoutFlip || withFlip;
}

// Example usage
int main() {
    // Construct example trees
    Node* T1 = new Node(1);
    T1->left = new Node(2);
    T1->right = new Node(3);
    T1->left->left = new Node(4);

    Node* T2 = new Node(1);
    T2->left = new Node(3);
    T2->right = new Node(2);
    T2->right->right = new Node(4);

    if (isIsomorphic(T1, T2)) {
        cout << "Yes, the trees are isomorphic." << endl;
    } else {
        cout << "No, the trees are not isomorphic." << endl;
    }

    return 0;
}
