// Helper function to print the Kth node from the end
Node* findKthFromEnd(Node* head, int& k) {
    // Base case: if we reach the end of the list, return nullptr
    if (head == nullptr) return nullptr;

    // Recursive call to go to the end of the list
    Node* node = findKthFromEnd(head->next, k);

    // When coming back from the recursive call, decrement k
    k--;

    // When k is 0, we have found the Kth node from the end
    if (k == 0) {
        return head;  // Return the node that is Kth from the end
    }

    // Return the node found in the previous recursive calls
    return node;
}

// Function to get the Kth node from the end
Node* getKthFromEnd(Node* head, int k) {
    return findKthFromEnd(head, k);
}


// iterative

// Function to find the Nth node from the end of the list
int getNthFromLast(Node* head, int n) {
    // Initialize two pointers: 'primary' and 'follower' both pointing to the head
    Node* primary = head;
    Node* follower = head;
    
    // Step 1: Move 'primary' n nodes ahead
    int count = 1;
    while (count < n) {
        // If 'primary' reaches the end before moving n nodes, n is larger than the list length
        if (primary->next == nullptr) return -1;
        primary = primary->next;
        count++;
    }
    
    // Step 2: Move both 'primary' and 'follower' one step at a time until 'primary' reaches the end
    while (primary->next != nullptr) {
        primary = primary->next;
        follower = follower->next;
    }
    
    // 'follower' is now at the Nth node from the end
    return follower->data;
}