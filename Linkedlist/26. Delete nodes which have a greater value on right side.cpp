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
