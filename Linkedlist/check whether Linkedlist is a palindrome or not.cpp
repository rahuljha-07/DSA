// Function to reverse a linked list and return the new head
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
    return prev;
}

// Function to check whether a linked list is palindrome
bool isPalindrome(Node* head) {
    // Edge case: If the list is empty or has only one element, it is a palindrome
    if (head == nullptr || head->next == nullptr) {
        return true;
    }

    // Step 1: Use slow and fast pointers to find the middle of the list
    Node* slow = head;
    Node* fast = head;
    
    // Move slow to the middle and fast to the end
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;          // slow moves one step at a time
        fast = fast->next->next;    // fast moves two steps at a time
    }

    // Step 2: Reverse the second half of the list
    slow = reverse(slow); // Reverse from the middle to the end
    
    // Step 3: Compare the first half and the reversed second half
    Node* firstHalf = head;
    Node* secondHalf = slow;
    
    while (secondHalf != nullptr) {
        if (firstHalf->data != secondHalf->data) {
            return false;  // If any data doesn't match, it's not a palindrome
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    // If we reach this point, it means the list is a palindrome
    return true;
}

// 1 -> 2 -> 3 <- 4 <- 5 