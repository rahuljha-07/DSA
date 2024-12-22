void deleteNode(Node* &head, int value) {
    if (head == nullptr) return; // If the list is empty, nothing to delete

    // Case 1: If the list has only one node and it matches the value
    if (head->next == head && head->data == value) {
        delete head;
        head = nullptr; // Set head to nullptr as the list is now empty
        return;
    }

    Node* temp = head;
    Node* prev = nullptr;

    // Case 2: If the node to delete is the head node
    if (head->data == value) {
        Node* last = head;
        
        // Traverse the list to find the last node
        while (last->next != head) {
            last = last->next;
        }
        
        // Update the last node's next to the second node
        last->next = head->next;
        
        // Move head to the next node and delete the old head
        temp = head;
        head = head->next;
        delete temp;
        return;
    }

    // Case 3: Traverse the list to find the node with the given value
    do {
        if (temp->data == value) {
            prev->next = temp->next; // Skip the node to delete
            delete temp;             // Delete the node
            return;
        }
        prev = temp;
        temp = temp->next;
    } while (temp != head);  // Loop back to the head if we haven't reached the end

    // If the value is not found, do nothing
}
