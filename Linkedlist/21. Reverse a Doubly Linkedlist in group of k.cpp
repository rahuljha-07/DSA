Node* reverseGroup(Node* head, int k) {
    if (!head) return nullptr;

    Node* curr = head;
    Node* temp = nullptr;
    Node* prev = nullptr;
    int count = 0;

    // Step 1: Reverse the first 'k' nodes using your logic
    while (curr != nullptr && count < k) {
        temp = curr->prev;        // Store previous node
        curr->prev = curr->next;  // Swap pointers
        curr->next = temp;        // Complete swap

        prev = curr;              // Update 'prev' (new head for the group)
        curr = curr->prev;        // Move to next node (using swapped pointer)
        count++;
    }

    // Step 2: Connect with the next group (recursive call)
    if (curr != nullptr) {
        head->next = reverseGroup(curr, k); // Recurse for next group
        if (head->next != nullptr) {
            head->next->prev = head;       // Maintain doubly link
        }
    }

    // 'prev' is the new head of this group
    return prev;
}
