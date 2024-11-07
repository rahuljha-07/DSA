// Function to move the last element to the front of the linked list
Node* moveLastToFront(Node* head) {
    if (head == nullptr || head->next == nullptr) return head; // Empty or single-node list
    
    Node* secondLast = nullptr;
    Node* last = head;

    // Traverse the list to find the last and second-last nodes
    while (last->next != nullptr) {
        secondLast = last;
        last = last->next;
    }

    // If there are two nodes, make the second-last node's next point to nullptr
    secondLast->next = nullptr;
    
    // Make the last node point to the head
    last->next = head;
    
    // Move the head pointer to the last node
    head = last;

    return head;
}