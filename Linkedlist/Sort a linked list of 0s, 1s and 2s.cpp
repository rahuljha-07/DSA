// Function to sort a linked list of 0s, 1s, and 2s using counting
Node* segregate(Node *head) {
    int count[3] = {0};  // Array to store the count of 0s, 1s, and 2s
    
    Node* temp = head;
    // Count the occurrences of 0, 1, and 2 in the list
    while (temp) {
        count[temp->data]++;  // Increment the count of the respective data
        temp = temp->next;
    }
    
    temp = head;
    int i = 0;
    // Update the linked list based on the counts
    while (temp) {
        if (count[i] == 0) {
            i++;  // Move to the next number if no more of the current number is left to assign
        } else {
            temp->data = i;  // Set the node's data to the current number
            count[i]--;  // Decrease the count for the current number
            temp = temp->next;  // Move to the next node
        }
    }
    
    return head;  // Return the head of the modified list
}

// Function to sort a linked list of 0s, 1s, and 2s using dummy nodes
Node* segregateUsingDummy(Node *head) {
    // Create dummy nodes for 0, 1, and 2
    Node *zeroDummy = new Node(0);  // Dummy node to store 0s
    Node *oneDummy = new Node(0);   // Dummy node to store 1s
    Node *twoDummy = new Node(0);   // Dummy node to store 2s
    
    // Pointers to the current nodes of the three dummy lists
    Node *zero = zeroDummy, *one = oneDummy, *two = twoDummy;
    Node *curr = head;  // Pointer to traverse the original list
    
    // Traverse the original list and divide nodes into 0, 1, and 2 lists
    while (curr) {
        if (curr->data == 0) {
            zero->next = curr;  // Add node to the zero list
            zero = zero->next;  // Move the zero pointer
        } else if (curr->data == 1) {
            one->next = curr;   // Add node to the one list
            one = one->next;    // Move the one pointer
        } else {
            two->next = curr;   // Add node to the two list
            two = two->next;    // Move the two pointer
        }
        curr = curr->next;  // Move to the next node in the original list
    }
    
    // Terminate the three lists
    two->next = nullptr;  // Last node of the two list should point to nullptr
    
    // Join the three lists: zero -> one -> two
    zero->next = oneDummy->next;  // Link the zero list to the one list
    one->next = twoDummy->next;   // Link the one list to the two list
    
    // The head of the sorted list is the next node of the zero dummy node
    Node *sortedHead = zeroDummy->next;
    
    // Clean up: delete dummy nodes
    delete zeroDummy;
    delete oneDummy;
    delete twoDummy;
    
    return sortedHead;  // Return the head of the sorted linked list
}
