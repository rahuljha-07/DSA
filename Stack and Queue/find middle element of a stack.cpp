#include <iostream>
using namespace std;

// Node structure for DLL
struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int val) : data(val), prev(nullptr), next(nullptr) {}
};

// Stack class with middle operations
class StackWithMiddle {
private:
    Node* head;   // Points to the head of the DLL
    Node* mid;    // Points to the middle of the DLL
    int count;    // Number of elements in the stack

public:
    StackWithMiddle() : head(nullptr), mid(nullptr), count(0) {}

    // Push an element onto the stack
    void push(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        
        // Link the new node at the beginning
        if (head) head->prev = newNode;
        head = newNode;
        count++;

        // Update mid pointer
        if (count == 1) {
            mid = head;
        } else if (count % 2 == 0) {
            mid = mid->prev;
        }
    }

    // Pop the top element from the stack
    int pop() {
        if (count == 0) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        
        int data = head->data;
        Node* temp = head;
        head = head->next;
        if (head) head->prev = nullptr;
        
        delete temp;
        count--;

        // Update mid pointer
        if (count % 2 != 0) {
            mid = mid->next;
        }

        return data;
    }

    // Find the middle element of the stack
    int findMiddle() const {
        if (count == 0) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        return mid->data;
    }

    // Delete the middle element of the stack
    void deleteMiddle() {
        if (count == 0) {
            cout << "Stack is empty." << endl;
            return;
        }
        
        Node* temp = mid;
        int midData = mid->data;

        // Update the mid pointer and count
        if (count == 1) {
            head = nullptr;
            mid = nullptr;
        } else if (count % 2 == 0) { // Move mid pointer to next if count is even
            mid = mid->next;
        } else { // Move mid pointer to prev if count is odd
            mid = mid->prev;
        }

        // Update links to remove the middle node
        if (temp->prev) temp->prev->next = temp->next;
        if (temp->next) temp->next->prev = temp->prev;

        delete temp;
        count--;

        cout << "Deleted middle element: " << midData << endl;
    }
};

int main() {
    StackWithMiddle stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);

    cout << "Middle element: " << stack.findMiddle() << endl; // Output: 30

    stack.deleteMiddle();
    cout << "Middle element after deletion: " << stack.findMiddle() << endl; // Output: 20

    stack.push(60);
    cout << "Middle element after push: " << stack.findMiddle() << endl; // Output: 30

    stack.pop();
    cout << "Middle element after pop: " << stack.findMiddle() << endl; // Output: 20

    return 0;
}
