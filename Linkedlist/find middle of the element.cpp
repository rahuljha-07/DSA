// Function to find the middle of the linked list using slow and fast pointers
int findMiddle(Node* head) {
    // Check if the list is empty
    if (head == NULL) return -1;
    
    // Initialize two pointers: slow and fast
    Node* slow = head;
    Node* fast = head;
    
    // Traverse the list with fast moving two steps at a time and slow moving one step at a time
    while (fast && fast->next) {
        slow = slow->next;       // Move slow pointer one step
        fast = fast->next->next; // Move fast pointer two steps
    }
    
    // When fast reaches the end, slow will be at the middle
    return slow->data; // Return the data of the middle node
}
