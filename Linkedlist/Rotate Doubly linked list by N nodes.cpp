#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

// Function to find the length of the doubly linked list
int length(Node* head) {
    int len = 0;
    Node* temp = head;
    while (temp != nullptr) {
        len++;
        temp = temp->next;
    }
    return len;
}

// Function to rotate the doubly linked list by N nodes
Node* rotate(Node* head, int N) {
    if (head == nullptr || head->next == nullptr || N == 0) {
        return head;  // No rotation needed for empty or single-node list, or N=0
    }

    // Step 1: Find the length of the list
    int len = length(head);

    // Step 2: If N is greater than the length of the list, take N % length to avoid extra rotations
    N = N % len;
    if (N == 0) return head;  // No rotation needed if N is a multiple of length

    // Step 3: Traverse till N node
    Node* newTail = head;
    for (int i = 1; i < N; i++) {
        newTail = newTail->next;
    }

    // Step 4: The (N + 1)th node becomes the new head
    Node* newHead = newTail->next;
 
    // Step 5: Update the pointers to rotate the list
    newTail->next = nullptr;  // New tail points to null
    newHead->prev = nullptr;  // New head's previous pointer becomes null

    // Find the last node of the list (old tail)
    Node* oldTail = newHead;
    while (oldTail->next != nullptr) {
        oldTail = oldTail->next;
    }

    // The old tail's next pointer should now point to the old head
    oldTail->next = head;
    head->prev = oldTail;

    // Step 6: Return the new head of the list
    return newHead;
}

// Function to print the doubly linked list
void printList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

// Helper function to insert nodes at the end of the doubly linked list
Node* insert(Node* head, int data) {
    Node* newNode = new Node(data);
    if (head == nullptr) {
        return newNode;
    }
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

int main() {
    Node* head = nullptr;

    // Create a doubly linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = insert(head, 1);
    head = insert(head, 2);
    head = insert(head, 3);
    head = insert(head, 4);
    head = insert(head, 5);

    cout << "Original List: ";
    printList(head);

    int N = 2;  // Rotate the list by 2 nodes
    head = rotate(head, N);

    cout << "List after rotating by " << N << " nodes: ";
    printList(head);

    return 0;
}
