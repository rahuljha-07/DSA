bool detectCycle(Node* head) {
    if (head == nullptr) return false; // If the list is empty, there's no cycle

    // Initialize two pointers
    Node* slow = head;
    Node* fast = head;

    // Loop to move the pointers through the list
    while (fast->next && fast->next->next) {
        // Move the fast pointer two steps and slow pointer one step
        fast = fast->next->next;
        slow = slow->next;

        // If the two pointers meet, a cycle exists
        if (slow == fast) return true;
    }

    // If the loop ends, no cycle was found
    return false;
}