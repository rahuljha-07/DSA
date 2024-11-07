Node* findIntersection(Node* head1, Node* head2) {
    // Initialize two pointers for traversing both lists
    Node* first = head1;
    Node* second = head2;
    
    // Initialize the result list
    Node* res = NULL;
    Node* cur = NULL;
    
    // Traverse both lists until one is exhausted
    while (first && second) {
        // If first list node's data is smaller, move the first pointer
        if (first->data < second->data) {
            first = first->next;
        }
        // If second list node's data is smaller, move the second pointer
        else if (first->data > second->data) {
            second = second->next;
        }
        // If both nodes have the same data, add to result list
        else {
            // Create a new node with the common value
            Node* temp = new Node(first->data);
            
            // If result list is empty, initialize it with the new node
            if (res == NULL) {
                res = temp;
                cur = temp;
            }
            // Otherwise, append to the result list
            else {
                cur->next = temp;
                cur = cur->next;
            }
            
            // Move both pointers to the next node
            first = first->next;
            second = second->next;
        }
    }
    
    // Return the head of the intersection list
    return res;
}
