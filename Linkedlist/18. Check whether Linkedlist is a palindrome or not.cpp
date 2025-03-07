Node* reverse(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr) {
        Node* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}

bool isPalindrome(Node* head) {
    if (!head || !head->next) return true;

    // Step 1: Find the middle using slow & fast pointers
    Node* slow = head;
    Node* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Step 2: Split the list into two halves
    Node* newHead = slow->next;
    slow->next = nullptr; // Break the list into two

    // Step 3: Reverse the second half
    Node* revHead = reverse(newHead);

    // Step 4: Compare both halves
    Node* firstHalf = head;
    Node* secondHalf = revHead;

    while (secondHalf) {
        if (firstHalf->data != secondHalf->data) {
            return false; // Not a palindrome
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    return true;
}


// 1 -> 2 -> 3 <- 4 <- 5 