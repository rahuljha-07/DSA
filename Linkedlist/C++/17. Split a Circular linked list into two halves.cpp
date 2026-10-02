// Function to detect and remove the loop in the linked list
void removeLoop(Node* head) {
    if (head == nullptr || head->next == nullptr) return; // If the list is empty or has only one node, no loop possible

    Node* slow = head;
    Node* fast = head;

    // Step 1: Detect if there's a cycle in the list
    bool hasCycle = false;
    while (fast->next && fast->next->next) {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast) { // If slow and fast meet, there is a cycle
            hasCycle = true;
            break;
        }
    }

    // If there’s no cycle, return as there’s nothing to remove
    if (!hasCycle) return;

    // Step 2: Find the starting point of the loop
    slow = head; // Reset slow to the head of the list
    if (slow == fast) {
        // Special case: If the cycle starts at the head of the list
        while (fast->next != slow) {
            fast = fast->next;
        }
    } else {
        // Move both pointers one step at a time until they meet at the start of the loop
        while (slow->next != fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
    }

    // Step 3: Remove the loop by setting the next of the last node in the loop to NULL
    fast->next = nullptr;
}

// Function to split the circular linked list into two halves
void splitList(Node* head) {
    if (head == nullptr || head->next == nullptr) return; // List is empty or has only one node

    // Step 1: Remove the loop if present
    removeLoop(head);

    // Step 2: Initialize slow and fast pointers to find the middle of the list
    Node* slow = head;
    Node* fast = head;

    // Traverse the list to find the middle using slow and fast pointers
    while (fast != nullptr && fast->next != nullptr) {
        fast = fast->next->next;  // Move fast pointer two steps at a time
        slow = slow->next;        // Move slow pointer one step at a time
    }

    // At this point, slow points to the middle of the list
    Node* secondHalf = slow->next; // The second half of the list starts from slow->next
    slow->next = nullptr;          // End the first half of the list

    // Step 3: Print the two halves (or return them if needed)
    // Optionally: If you need to return the two halves, you can return head (first half) and secondHalf (second half)
    // For now, let's just print the two halves for demonstration
    cout << "First half: ";
    printList(head);
    cout << "Second half: ";
    printList(secondHalf);
}
