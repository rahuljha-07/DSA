// Function to remove duplicates from a sorted linked list
Node* removeDuplicates(Node* head) {
    // If the list is empty or has only one element, there's no need to remove duplicates
    if (head == nullptr || head->next == nullptr) return head;

    // Initialize two pointers:
    // 'current' points to the node currently being checked for duplicates
    // 'nextNode' is the node following 'current', which we compare with 'current'
    Node* current = head;
    Node* nextNode = head->next;

    // Traverse the list until we reach the end
    while (nextNode != nullptr) {
        // If 'current' and 'nextNode' have different data, move both pointers forward
        if (current->data != nextNode->data) {
            current = nextNode;
            nextNode = nextNode->next;
        } else {
            // If 'current' and 'nextNode' have the same data, there's a duplicate
            // Skip the duplicate by changing 'current's next pointer to the node after 'nextNode'
            current->next = nextNode->next;

            // Delete the duplicate node
            delete nextNode;

            // Move 'nextNode' to the next node in the list
            nextNode = current->next;
        }
    }

    // Return the head of the modified list
    return head;
}