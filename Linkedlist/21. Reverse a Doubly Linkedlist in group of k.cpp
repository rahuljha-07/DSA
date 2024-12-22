Node* reverseInGroupsRecursive(Node* head, int k) {
    if (!head) return nullptr; // Base case: empty list

    Node* curr = head;
    Node* prev = nullptr;
    int count = 0;

    // Reverse the first 'k' nodes
    while (curr && count < k) {
        Node* nextNode = curr->next;
        curr->next = prev;
        curr->prev = nextNode;

        prev = curr;
        curr = nextNode;
        count++;
    }

    // After reversing, `prev` is the new head of this group
    // Connect the reversed group to the next group
    if (curr) {
        head->next = reverseInGroupsRecursive(curr, k); // Recur for the next group
        if (head->next) {
            head->next->prev = head; // Update the `prev` pointer of the new group's head
        }
    }

    // `prev` is now the new head of the reversed group
    return prev;
}