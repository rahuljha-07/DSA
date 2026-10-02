#include <iostream>
#include <string>
using namespace std;

// Definition for a binary tree node.
struct Node {
    int value;
    Node* left;
    Node* right;
    Node(int x) : value(x), left(nullptr), right(nullptr) {}
};

int start = 0; // Global variable for tracking position in the string

// Function to construct a binary tree from a string
Node* constructTree(string s) {
    if (s.empty()) return nullptr;
    return stringToTree(s);
}

// Helper function to recursively build the tree
Node* stringToTree(string& s) {
    if (start >= s.length()) return nullptr;
    
    bool neg = false;
    if (s[start] == '-') {
        neg = true;
        start++;
    }
    
    int num = 0;
    while (start < s.length() && isdigit(s[start])) {
        num = num * 10 + (s[start] - '0');
        start++;
    }
    
    if (neg) num = -num; // If the number is negative

    Node* root = new Node(num);
    
    // If the string has no more characters, return the root end node
    if (start >= s.length()) return root;

    // If the next character is '(', it indicates a left child
    if (start < s.length() && s[start] == '(') {
        start++; // Skip '('
        root->left = stringToTree(s);
    }

    // If the next character is ')', it indicates the end of left child
    if (start < s.length() && s[start] == ')') {
        start++; // Skip ')'
        return root;
    }

    // If the next character is '(', it indicates a right child
    if (start < s.length() && s[start] == '(') {
        start++; // Skip '('
        root->right = stringToTree(s);
    }

    // If the next character is ')', it indicates the end of right child
    if (start < s.length() && s[start] == ')') {
        start++; // Skip ')'
        return root;
    }

    return root;
}

// Function to print the tree (in-order traversal)
void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->value << " ";
    inorder(root->right);
}

int main() {
    string s = "1(2(4)(5))(3(6)(7))"; // Example input string
    Node* root = constructTree(s);
    inorder(root); // Output the tree
    return 0;
}
