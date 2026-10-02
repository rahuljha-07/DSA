bool isCircular(Node *head) {
    // If the list is empty, it's not circular
    if (head == NULL) return false;

    // Initialize slow and fast pointers
    Node *slow = head;
    Node *fast = head;

    // Traverse the list
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;            // Move slow pointer one step
        fast = fast->next->next;      // Move fast pointer two steps

        // If slow and fast meet, there's a cycle (circular list)
        if (slow == fast) {
            return true;
        }
    }

    // If fast or fast->next becomes NULL, the list is not circular
    return false;
}
