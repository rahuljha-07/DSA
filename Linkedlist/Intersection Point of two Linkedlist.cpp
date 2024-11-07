#include <iostream>
#include <cmath>  // For abs() function

// Definition of Node structure
struct Node {
    int data;
    Node* next;

    // Constructor for creating a new node
    Node(int value) : data(value), next(nullptr) {}
};

// Function to find the intersection point of two linked lists
int intersectPoint(Node* head1, Node* head2) {
    // Initialize pointers for both linked lists
    Node* p = head1;
    Node* q = head2;
    
    // Variables to store the lengths of both linked lists
    int diff, c1 = 0, c2 = 0;
    
    // Step 1: Calculate the length of the first linked list (head1)
    while (p) {
        p = p->next;
        c1++;  // Increment the length of list 1
    }
    
    // Step 2: Calculate the length of the second linked list (head2)
    while (q) {
        q = q->next;
        c2++;  // Increment the length of list 2
    }
    
    // Step 3: Calculate the difference in lengths of the two lists
    diff = abs(c1 - c2);  // Absolute difference between the lengths
    
    // Reset the pointers to the heads of the lists
    p = head1;
    q = head2;
    
    // Step 4: Align both lists by moving the pointer of the longer list ahead by the difference in lengths
    if (c1 > c2) {
        // Move pointer p (head1) forward by the difference in length
        for (int i = 0; i < diff; i++) {
            p = p->next;
        }
    }
    else if (c2 > c1) {
        // Move pointer q (head2) forward by the difference in length
        for (int i = 0; i < diff; i++) {
            q = q->next;
        }
    }
    
    // Step 5: Traverse both lists simultaneously and check for intersection
    while (p != q) {
        p = p->next;  // Move pointer p to the next node
        q = q->next;  // Move pointer q to the next node
    }
    
    // Step 6: If p and q meet, return the intersection point, else return -1
    if (p) return p->data;  // Return the data of the intersection node
    return -1;  // No intersection found, return -1
}
