Node* reverse(Node *head) {
    Node *p = head;
    Node *q = NULL;
    Node *r = NULL;
    while (p != NULL) {
        r = q;
        q = p;
        p = p->next;
        q->next = r;
    }
    head = q;
    return head;
}

Node* compute(Node *head) {
    // Step 1: Reverse the list
    head = reverse(head);
    
    // Step 2: Traverse the reversed list and remove nodes with smaller values
    Node* cur = head;
    int max = head->data;
    Node* prev = head;
    cur = cur->next;
    while (cur) {
        if (cur->data >= max) {
            max = cur->data;
            prev = cur;
            cur = cur->next;
        } else {
            prev->next = cur->next;  // Remove the current node
            cur = prev->next;
        }
    }

    // Step 3: Reverse the list back to restore the original order
    head = reverse(head);
    return head;
}

Node* deleteNodes(Node* head, int& maxi) {
    // Base case: If the list is empty, return NULL
    if (head == nullptr) {
        maxi = INT_MIN; // Reset maxi when the list is empty
        return nullptr;
    }

    // Base case: If we are at the last node, update maxi and return the node
    if (head->next == nullptr) {
        maxi = head->data;
        return head; // Keep the last node
    }

    // Recursive call: Process the rest of the list
    Node* newHead = deleteNodes(head->next, maxi);

    // Check the current node against the updated maxi
    if (head->data < maxi) {
        // If the current node's value is smaller than maxi, delete it
        delete head;
        return newHead;
    }

    // Otherwise, keep the current node and update maxi
    maxi = head->data;
    head->next = newHead;
    return head;
}

// Wrapper function
Node* deleteNodes(Node* head) {
    int maxi = INT_MIN;
    return deleteNodes(head, maxi);
}
