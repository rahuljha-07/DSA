#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> replaceWithLeastGreater(vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, -1);  // Initialize the result with -1
    
    set<int> s;  // Sorted set to keep track of elements we've processed
    
    // Traverse the array from right to left
    for (int i = n - 1; i >= 0; --i) {
        auto it = s.upper_bound(arr[i]);  // Find the first element greater than arr[i]
        
        // If a greater element is found, it will be the least greater element
        if (it != s.end()) {
            result[i] = *it;  // Assign the least greater element
        }
        
        // Insert the current element into the set
        s.insert(arr[i]);
    }
    
    return result;
}

int main() {
    vector<int> arr = {8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28};
    vector<int> result = replaceWithLeastGreater(arr);
    
    for (int num : result) {
        cout << num << " ";
    }
    
    return 0;
}

// Node definition for the BST
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(NULL), right(NULL) {}
};

// Function to insert a node in BST and find the least greater element
Node* insert(Node* root, int key, int& successor) {
    if (root == NULL) 
        return new Node(key);
        
    if (key < root->data) {
        successor = root->data;
        root->left = insert(root->left, key, successor);
    } else {
        root->right = insert(root->right, key, successor);
    }
    return root;
}

vector<int> replaceWithLeastGreater(vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, -1);
    Node* root = NULL;
    
    for (int i = n - 1; i >= 0; --i) {
        int successor = -1;
        root = insert(root, arr[i], successor);
        result[i] = successor;
    }
    
    return result;
}
