// Function to split the linked list into two halves using a slow and fast pointer approach.
void findmiddle(Node* cur, Node** first, Node** second) {
    Node* slow = cur;
    Node* fast = cur;

    // Move fast by 2 steps and slow by 1 step until fast reaches the end of the list.
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Split the list at the middle point.
    *first = cur;
    *second = slow->next;
    slow->next = nullptr; // End the first half.
}

// Function to merge two sorted linked lists iteratively.
Node* mergeboth(Node* first, Node* second) {
    Node dummy;
    Node* tail = &dummy;

    while (first && second) {
        if (first->data <= second->data) {
            tail->next = first;
            first = first->next;
        } else {
            tail->next = second;
            second = second->next;
        }
        tail = tail->next;
    }
    tail->next = (first) ? first : second;
    return dummy.next;
}

// Recursive function to perform merge sort on the linked list.
void mergesorting(Node** head) {
    Node* cur = *head;
    Node* first;
    Node* second;

    // Base case: if the list has zero or one element, it's already sorted.
    if (!cur || !cur->next) return;

    // Step 1: Split the list into two halves using findmiddle.
    findmiddle(cur, &first, &second);

    // Step 2: Sort each half.
    mergesorting(&first);
    mergesorting(&second);

    // Step 3: Merge the sorted halves.
    *head = mergeboth(first, second);
}

// Main function to sort the linked list using Merge Sort.
Node* mergeSort(Node* head) {
    mergesorting(&head);
    return head;
}
