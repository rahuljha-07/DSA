// Global variable to keep track of the index in the preorder traversal
int preorderIndex = 0;

// Function to build the binary tree from preorder and inorder traversals
Node* buildTreeFromPreorderInorder(const vector<int>& inorder, const vector<int>& preorder, int leftBound, int rightBound, unordered_map<int, int>& inorderMap) {
    // Base case: if the current range is invalid (left > right), return NULL
    if (leftBound > rightBound) {
        return nullptr;
    }

    // Create a new node with the current value from preorder and increment preorder index
    Node* currentNode = new Node(preorder[preorderIndex++]);

    // If there's only one element in the range, it must be a leaf node
    if (leftBound == rightBound) {
        return currentNode;
    }

    // Find the index of the current node in inorder traversal
    int inorderIndex = inorderMap[currentNode->data];

    // Recursively build the left and right subtrees
    currentNode->left = buildTreeFromPreorderInorder(inorder, preorder, leftBound, inorderIndex - 1, inorderMap);
    currentNode->right = buildTreeFromPreorderInorder(inorder, preorder, inorderIndex + 1, rightBound, inorderMap);

    return currentNode;
}

// Function to build the binary tree from preorder and inorder traversals
Node* buildTree(const vector<int>& inorder, const vector<int>& preorder, int n) {
    preorderIndex = 0;  // Reset the preorder index
    unordered_map<int, int> inorderMap;

    // Create a map of inorder values to their indices for quick lookup
    for (int i = 0; i < n; ++i) {
        inorderMap[inorder[i]] = i;
    }

    // Start building the tree
    return buildTreeFromPreorderInorder(inorder, preorder, 0, n - 1, inorderMap);
}

// for post order traversal and inorder run loop from behind thats it