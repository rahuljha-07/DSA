// Function to remove duplicates from an unsorted linked list using a set
Node* removeDuplicates(Node* head) {
    if (head == nullptr) return nullptr;  // Return null if the list is empty

    unordered_set<int> seen;  // Set to track unique values
    Node* current = head;
    Node* nextNode = head->next;  // Start from the next node after head

    seen.insert(current->data);  // Push the head's data into the set

    // Traverse the list starting from the second node
    while (nextNode != nullptr) {
        // If the value is already in the set, skip this node
        if (seen.find(nextNode->data) != seen.end()) {
            current->next = nextNode->next;  // Skip the duplicate node
            delete nextNode;  // Free memory
        } else {
            seen.insert(nextNode->data);  // Add current data to the set
            current = nextNode;  // Move current pointer forward
        }
        nextNode = nextNode->next;  // Move nextNode to the next node
    }

    return head;  // Return the modified list
}