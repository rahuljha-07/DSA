#include<iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

Node* reverseGroup(Node* head, int k) {
    if (!head) return nullptr;

    Node* curr = head;
    Node* temp = nullptr;
    Node* prev = nullptr;
    int count = 0;

    // Step 1: Reverse the first 'k' nodes using your logic
    while (curr != nullptr && count < k) {
        temp = curr->prev;        // Store previous node
        curr->prev = curr->next;  // Swap pointers
        curr->next = temp;        // Complete swap

        prev = curr;              // Update 'prev' (new head for the group)
        curr = curr->prev;        // Move to next node (using swapped pointer)
        count++;
    }

    // Step 2: Connect with the next group (recursive call)
    if (curr != nullptr) {
        head->next = reverseGroup(curr, k); // Recurse for next group
        if (head->next != nullptr) {
            head->next->prev = head;       // Maintain doubly link
        }
    }

    // 'prev' is the new head of this group
    return prev;
}

// Function to print the doubly linked list
void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// Driver function for testing
int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->prev = head;
    head->next->next = new Node(3);
    head->next->next->prev = head->next;
    head->next->next->next = new Node(4);
    head->next->next->next->prev = head->next->next;
    head->next->next->next->next = new Node(5);
    head->next->next->next->next->prev = head->next->next->next;
    head->next->next->next->next->next = new Node(6);
    head->next->next->next->next->next->prev = head->next->next->next->next;
    head->next->next->next->next->next->next = new Node(7);
    head->next->next->next->next->next->next->prev = head->next->next->next->next->next;
    head->next->next->next->next->next->next->next = new Node(8);
    head->next->next->next->next->next->next->next->prev = head->next->next->next->next->next->next;

    cout << "Original list: ";
    printList(head);

    int k = 3;
    head = reverseGroup(head, k);

    cout << "Reversed in groups of " << k << ": ";
    printList(head);

    return 0;
}