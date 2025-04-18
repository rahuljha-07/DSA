// Function to reverse the linked list
Node* reverse(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    Node* nextNode = nullptr;

    while (curr != nullptr) {
        nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }

    return prev;  // New head after reversing
}

// Function to add one to the number represented by the linked list
Node* addOne(Node *head) {
    head = reverse(head);  // Step 1: Reverse the linked list

    bool carry = true;  // To track carry over
    Node* p = head;  // Pointer to traverse the list

    while (p != nullptr && carry == true) {
        // If it's the last node and it has a 9, add a new node for carry
        if (p->next == nullptr && p->data == 9) {
            p->data = 0;  // Set the last node to 0 (carry)
            Node* temp = new Node(1);  // Create a new node for carry
            p->next = temp;  // Link the new node
            p = temp;  // Move to the new node
        } 
        // If the current node is 9, set it to 0 and move to the next
        else if (p->data == 9) {
            p->data = 0;  // Set current node to 0
            p = p->next;  // Move to the next node
        } 
        // If it's not 9, just add 1 and stop
        else {
            p->data = p->data + 1;  // Add 1 to the current node
            p = p->next;  // Move to the next node
            carry = false;  // No carry is left, so break the loop
        }
    }

    head = reverse(head);  // Step 2: Reverse the list back to original order
    return head;  // Return the modified list
}

//using recursion

// Recursive function to add +1 to the linked list
int addOneUtil(Node* head) {
    // Base case: If the list is empty, return carry as 1
    if (head == nullptr)
        return 1;

    // Recur for the next node
    int carry = addOneUtil(head->next);

    // Add carry to the current node's data
    int sum = head->data + carry;
    head->data = sum % 10; // Update the current node's data
    return sum / 10;       // Return carry for the previous node
}

// Function to add +1 to the linked list
Node* addOne(Node* head) {
    // Add one to the list and get the final carry
    int carry = addOneUtil(head);

    // If there's a carry remaining, add a new node at the beginning
    if (carry) {
        Node* newHead = new Node(carry);
        newHead->next = head;
        head = newHead;
    }
    return head;
}