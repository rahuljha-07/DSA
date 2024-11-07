// Function to reverse a doubly linked list
Node* reverse(Node* head) {
    if (head == nullptr) return nullptr;

    Node* curr = head;
    Node* temp = nullptr;

    // Swap next and prev pointers for each node
    while (curr != nullptr) {
        temp = curr->prev;       // Store the previous pointer
        curr->prev = curr->next; // Swap next and prev
        curr->next = temp;       // Complete the swap
        curr = curr->prev;       // Move to the next node in original order
    }

    // After the loop, temp points to the new head
    if (temp != nullptr) {
        head = temp->prev;
    }

    return head;
}

// Recursive function to reverse a doubly linked list
Node* reverseRecursive(Node* curr) {
    if (curr == nullptr) return nullptr;   // Base case: empty list
    if (curr->next == nullptr) {           // Base case: last node becomes the new head
        curr->prev = curr->next;           // Set the prev to next (nullptr) as new head's prev should be nullptr
        return curr;                       // Return the new head
    }
    
    // Swap the next and prev pointers
    Node* temp = curr->prev;
    curr->prev = curr->next;
    curr->next = temp;

    // Recursive call for the next node (which is curr->prev after swap)
    return reverseRecursive(curr->prev);   // Returns the new head after complete reversal
}

// Recursive function to reverse the list, modifying head by reference
void reverseRecursive(Node*& head, Node* curr) {
    // Base case: if we reach the end of the list, update head and return
    if (curr->next == nullptr) {
        head = curr;           // Update head to the last node
        curr->prev = nullptr;   // Set the prev pointer of the new head to nullptr
        return;
    }

    // Recur for the next node
    reverseRecursive(head, curr->next);

    // Backtracking phase: update pointers to reverse the list
    Node* nextNode = curr->next;
    nextNode->next = curr;      // Set next node's next to current node
    curr->prev = nextNode;      // Set current node's prev to next node
    curr->next = nullptr;       // Set current node's next to nullptr as it becomes the last in reversed list
}

// Helper function to call the recursive function with head as reference
void reverse(Node*& head) {
    if (head == nullptr || head->next == nullptr) return; // If list is empty or has one node
    reverseRecursive(head, head);
}