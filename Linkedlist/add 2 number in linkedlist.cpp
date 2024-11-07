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

// Function to add two numbers represented by linked lists
Node* addTwoLists(Node* first, Node* second) {
    // Step 1: Reverse both the linked lists
    first = reverse(first);
    second = reverse(second);
    
    int sum = 0;  // Variable to store the sum of two digits
    int carry = 0;  // Variable to store the carry for the next digit
    Node* res = nullptr;  // The result linked list (initialized as null)

    // Step 2: Traverse both lists and add corresponding digits
    while (first != nullptr || second != nullptr) {
        // Add corresponding digits along with the carry (if any)
        sum = carry + (first ? first->data : 0) + (second ? second->data : 0);
        
        // Calculate the carry for the next iteration
        carry = sum / 10;
        
        // The new digit (ones place of the sum)
        sum = sum % 10;
        
        // Create a new node with the sum and add it to the result list
        Node* temp = new Node(sum);
        
        // If the result list is not empty, set the new node's next to the current result list
        if (res != nullptr) {
            temp->next = res;
        }
        
        // The new node becomes the result list's head
        res = temp;

        // Move to the next node in each list if they exist
        if (first) first = first->next;
        if (second) second = second->next;
    }

    // Step 3: If there's a carry left, create a new node with the carry
    if (carry > 0) {
        Node* temp = new Node(carry);
        temp->next = res;
        res = temp;
    }

    // Step 4: Return the result list (the sum of the two numbers)
    return res;
}