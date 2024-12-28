#include <iostream>
#include <unordered_set>
using namespace std;

// Definition for a binary tree node.
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Function to count pairs from two BSTs whose sum is equal to given value X
    int countPairs(Node* root1, Node* root2, int X) {
        if (!root1 || !root2) return 0; // Handle edge case when either BST is empty
        
        // Step 1: Traverse the first BST and store its elements in a hash set
        unordered_set<int> elements;
        storeElementsInSet(root1, elements);

        // Step 2: Traverse the second BST and count pairs that sum to X
        int count = 0;
        countPairsWithSet(root2, elements, X, count);

        return count;
    }

private:
    // Helper function to traverse the first BST and store elements in a hash set
    void storeElementsInSet(Node* root, unordered_set<int>& elements) {
        if (!root) return;
        storeElementsInSet(root->left, elements);
        elements.insert(root->data);
        storeElementsInSet(root->right, elements);
    }

    // Helper function to traverse the second BST and find pairs that sum to X
    void countPairsWithSet(Node* root, const unordered_set<int>& elements, int X, int& count) {
        if (!root) return;
        countPairsWithSet(root->left, elements, X, count);
        if (elements.count(X - root->data)) {
            count++;
        }
        countPairsWithSet(root->right, elements, X, count);
    }
};

// Helper function to create a simple BST (for testing)
Node* insertBST(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->data) root->left = insertBST(root->left, key);
    else root->right = insertBST(root->right, key);
    return root;
}

int main() {
    // Construct two sample BSTs
    Node* root1 = nullptr;
    root1 = insertBST(root1, 5);
    insertBST(root1, 3);
    insertBST(root1, 7);
    insertBST(root1, 2);
    insertBST(root1, 4);

    Node* root2 = nullptr;
    root2 = insertBST(root2, 10);
    insertBST(root2, 6);
    insertBST(root2, 15);
    insertBST(root2, 3);
    insertBST(root2, 8);

    int targetSum = 9;

    Solution solution;
    int pairCount = solution.countPairs(root1, root2, targetSum);

    cout << "Number of pairs with sum " << targetSum << ": " << pairCount << endl;

    return 0;
}
