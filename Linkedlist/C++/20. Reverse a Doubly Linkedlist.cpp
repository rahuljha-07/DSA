#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

// Function to reverse a doubly linked list
Node* reverse(Node* head) {
    if (head == nullptr) return nullptr;

    Node* curr = head;
    Node* temp = nullptr;

    // Swap next and prev pointers for each node
    while (curr != nullptr) {
        temp = curr->prev;       // Store the previous pointer
        curr->prev = curr->next; // Swap next and prev
        curr->next = temp;       // Complete the swap
        head = curr;             // Update head to the current node
        curr = curr->prev;       // Move to the next node in original order
    }

    return head; // Return the new head of the reversed list
}

// Recursive function to reverse the linked list
Node* reverseRecursive(Node* curr, Node*& revHead) {
    // Base case: If we reach the last node, set revHead to it
    if (curr == nullptr || curr->next == nullptr) {
        revHead = curr;
        return curr;  // Return last node (new tail)
    }

    // Recursive call to process the next node
    Node* newHead = reverseRecursive(curr->next, revHead);

    // Link the current node to the reversed list
    newHead->next = curr;
    curr->prev = newHead;
    curr->next = nullptr;  // Mark current node as the new tail

    return curr;  // Return current node to help in backtracking
}

// Wrapper function to initiate recursion
void reverse(Node*& head) {
    Node* revHead = nullptr;  // This will store the new head after reversal
    reverseRecursive(head, revHead);
    head = revHead;  // Update the head of the original list to the reversed list
}
