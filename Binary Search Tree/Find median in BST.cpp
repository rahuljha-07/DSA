#include <iostream>
#include <vector>
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

// Helper function to perform in-order traversal to count the total number of nodes in the BST
void inorderCount(Node* root, int &count) {
    if (!root) return;
    
    inorderCount(root->left, count);
    count++;  // Increment count for each node visited
    inorderCount(root->right, count);
}

// Helper function to perform in-order traversal and find the median (odd/even count)
void inorderFindMedian(Node* root, int &iteration, int k, vector<int> &v) {
    if (!root) return;
    
    inorderFindMedian(root->left, iteration, k, v);
    
    iteration++;  // Increment iteration count for each node visited
    
    // Collect the nodes we need for the median calculation
    if (v.size() < 2) {
        v.push_back(root->data);  // If the vector size is less than 2, just add the value
    } else {
        // If size is 2, shift the elements
        v[0] = v[1];  // Move the previous value to index 0
        v[1] = root->data;  // Add the current value to index 1
    }
    
    if (iteration == k) {
        return;  // Stop once we reach the k-th element
    }
    
    inorderFindMedian(root->right, iteration, k, v);
}

// Function to find the median of the BST
double findMedian(Node* root) {
    // Step 1: Count the total number of nodes in the BST
    int count = 0;
    inorderCount(root, count);
    
    // Step 2: Perform in-order traversal to find the median
    vector<int> result;
    
    int k = count / 2 + 1;  // Find the k-th element (middle element or second middle for even case)
    int iteration=0;
    inorderFindMedian(root, iteration, k, result);
    
    if (count % 2 == 1) {
        // If the number of nodes is odd, return the last value
        return result[1];
    } else {
        // If the number of nodes is even, return the average of the two middle values
        return (result[0] + result[1]) / 2.0;
    }
}

// Example BST
int main() {
    Node* root = new Node(5);
    root->left = new Node(3);
    root->right = new Node(8);
    root->left->left = new Node(2);
    root->left->right = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(9);

    // Find and print the median of the BST
    double median = findMedian(root);
    cout << "The median of the BST is: " << median << endl;

    return 0;
}
