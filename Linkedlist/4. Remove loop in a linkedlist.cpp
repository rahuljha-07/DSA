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
