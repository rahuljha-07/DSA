#include <iostream>

struct Node {
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

Node* reverseIterative(Node* head) {
    Node* prev = nullptr;
    Node* current = head;
    Node* next = nullptr;

    while (current != nullptr) {
        next = current->next;  // Save the next node
        current->next = prev;   // Reverse the link
        prev = current;         // Move prev up
        current = next;         // Move current up
    }
    return prev;  // New head of the reversed list
}



Node* reverseRecursive(Node* head) {
    // Base case: empty list or end of list reached
    if (head == nullptr || head->next == nullptr)
        return head;

    // Reverse the rest of the list
    Node* newHead = reverseRecursive(head->next);

    // Reverse the link for current node
    head->next->next = head;
    head->next = nullptr;

    return newHead;
}
