#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

// Function to insert a new node at the end of the doubly linked list
void append(Node*& head, int data) {
    Node* newNode = new Node(data);
    if (!head) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

// Function to print the triplets whose sum is equal to a given value X
void printTripletsWithSum(Node* head, int X) {
    if (!head) return;

    // Find tail node
    Node* tail = head;
    while (tail->next) {
        tail = tail->next;
    }

    bool found = false;

    // Iterate through the DLL with the first element fixed
    for (Node* first = head; first != tail->prev; first = first->next) {
        Node* left = first->next;
        Node* right = tail;

        // Two-pointer approach to find the pair for the fixed element
        while (left != right) {
            int sum = first->data + left->data + right->data;
            if (sum == X) {
                cout << "(" << first->data << ", " << left->data << ", " << right->data << ")\n";
                found = true;

                // Move left pointer to avoid duplicates
                Node* tempLeft = left;
                while (left && left->data == tempLeft->data) {
                    left = left->next;
                }

                // Move right pointer to avoid duplicates
                Node* tempRight = right;
                while (right && right->data == tempRight->data) {
                    right = right->prev;
                }
            } 
            else if (sum < X) {
                left = left->next;  // Increase sum
            } 
            else {
                right = right->prev;  // Decrease sum
            }
        }
    }

    if (!found) {
        cout << "No triplets found with sum " << X << endl;
    }
}

// Helper function to print the doubly linked list (for testing purposes)
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " <-> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

int main() {
    // Create a doubly linked list: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
    Node* head = nullptr;
    append(head, 1);
    append(head, 2);
    append(head, 4);
    append(head, 5);
    append(head, 6);
    append(head, 8);
    append(head, 9);

    int target = 15;  // Given sum for triplets

    // Print the triplets whose sum is equal to the target
    cout << "Triplets with sum " << target << " are:" << endl;
    printTripletsWithSum(head, target);

    return 0;
}
