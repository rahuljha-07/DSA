// Define the structure for the linked list node
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Function to rearrange nodes in the list so that all even nodes appear before odd nodes
Node* divide(int N, Node* head) {
    // If the list is empty or has only one node, return as is
    if (!head || !head->next) return head;
    
    // Dummy nodes to start the even and odd lists
    Node* evenDummy = new Node(0); // Dummy head for even numbers
    Node* oddDummy = new Node(0);  // Dummy head for odd numbers
    Node* even = evenDummy; // Pointer to build the even list
    Node* odd = oddDummy;   // Pointer to build the odd list
    Node* current = head;   // Pointer to traverse the original list
    
    // Traverse the list and separate nodes into even and odd lists
    while (current) {
        if (current->data % 2 == 0) {
            even->next = current;  // Link even node
            even = even->next;     // Move even pointer forward
        } else {
            odd->next = current;   // Link odd node
            odd = odd->next;       // Move odd pointer forward
        }
        current = current->next; // Move to the next node
    }
    
    // Connect the end of even list to the start of odd list
    even->next = oddDummy->next;
    
    // End the odd list
    odd->next = nullptr;
    
    // Update head to point to the start of the new list (first even node)
    head = evenDummy->next;
    
    // Free the dummy nodes as they are no longer needed
    delete evenDummy;
    delete oddDummy;
    
    return head;
}