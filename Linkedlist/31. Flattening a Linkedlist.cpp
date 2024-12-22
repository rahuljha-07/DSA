Node* mergeboth(Node* first, Node* second) {
    // Dummy node is used to simplify the merge process
    Node* tail = nullptr; // This will track the last node in the merged list

    // If one of the lists is empty, return the other list
    if (!first) return second;
    if (!second) return first;

    // Initialize the head of the merged list
    if (first->data <= second->data) {
        tail = first;
        first = first->bottom;
    } else {
        tail = second;
        second = second->bottom;
    }

    Node* head = tail; // Head points to the start of the merged list

    // Merge both lists
    while (first && second) {
        if (first->data <= second->data) {
            tail->bottom = first;
            first = first->bottom;
        } else {
            tail->bottom = second;
            second = second->bottom;
        }
        tail = tail->bottom;
    }

    // Attach the remaining part of the non-empty list
    if (first) {
        tail->bottom = first;
    } else {
        tail->bottom = second;
    }

    return head; // Return the head of the merged list
}

// Recursive flatten function to merge the bottom lists
Node* flatten(Node* head) {
    if (!head || !head->next) {
        return head;  // Base case: single node or end of the list
    }

    // Flatten the next part of the list
    Node* nextNode = flatten(head->next);

    // Merge the current node's bottom list with the flattened next part
    head = mergeboth(head, nextNode);

    return head;
}