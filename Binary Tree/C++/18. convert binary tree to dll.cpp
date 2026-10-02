// Global pointers to keep track of the head and tail of the DLL
Node* head = nullptr;
Node* tail = nullptr;

// Function to convert the binary tree to a doubly linked list
Node* bToDLL(Node* root) {
    // Base case: if the tree is empty, return NULL
    if (!root) return nullptr;

    // Recursively convert the left subtree to DLL
    bToDLL(root->left);

    // If the tail is null, it means this is the first node, so set the head to it
    if (!tail) {
        head = root;
    } else {
        // Otherwise, link the current root node to the DLL
        root->left = tail;    // Set the previous pointer of the current node to the tail
        tail->right = root;   // Set the next pointer of the tail node to the current root
    }

    // Move the tail to the current node after processing
    tail = root;

    // Recursively convert the right subtree to DLL
    bToDLL(root->right);

    // Return the head of the doubly linked list
    return head;
}