Node* reverseGroupRecursive(Node* head, int k) {
    if (!head) return nullptr;

    Node* current = head;
    Node* prev = nullptr;
    Node* next = nullptr;
    int count = 0;

    // Reverse first k nodes
    while (current && count < k) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
        count++;
    }

    // Recursively call for the rest of the list
    if (next) {
        head->next = reverseGroupRecursive(next, k);
    }

    // prev is now the head of the reversed group
    return prev;
}
