// Function to find the starting point of the loop
Node* findLoopStart(Node* head) {
    if (head == nullptr || head->next == nullptr) return nullptr; // No loop possible if list is empty or has only one node

    Node* slow = head;
    Node* fast = head;

    // Step 1: Detect if there’s a loop in the list
    bool hasCycle = false;
    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast) { // If slow and fast meet, a cycle is detected
            hasCycle = true;
            break;
        }
    }

    // If there's no cycle, return nullptr
    if (!hasCycle) return nullptr;

    // Step 2: Find the starting point of the loop
    slow = head; // Reset slow pointer to the head
    while (slow != fast) {
        slow = slow->next; // Move both pointers one step at a time
        fast = fast->next;
    }

    // The point where slow and fast meet again is the starting point of the loop
    return slow;
}