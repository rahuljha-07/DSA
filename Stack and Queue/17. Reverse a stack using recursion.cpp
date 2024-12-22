#include <iostream>
#include <stack>

using namespace std;

// Function to print the elements of the stack without modifying it
void printStack(const stack<int>& s) {
    stack<int> temp = s; // Create a copy to preserve the original stack
    while (!temp.empty()) {
        cout << temp.top() << " ";
        temp.pop();
    }
    cout << endl;
}

// Recursive function to insert an element at the bottom of the stack
void insertAtBottom(stack<int>& s, int element) {
    if (s.empty()) {
        s.push(element);
        return;
    }
    int topElement = s.top();
    s.pop();
    insertAtBottom(s, element);
    s.push(topElement);
}

// Recursive function to reverse the stack
void performReverse(stack<int>& s) {
    if (s.empty()) {
        return;
    }
    int topElement = s.top();
    s.pop();
    performReverse(s);
    insertAtBottom(s, topElement);
}

// Function to reverse the stack using recursion
void reverseStack(stack<int>& s) {
    performReverse(s);
}

// Example usage
int main() {
    stack<int> s;

    // Pushing some elements onto the stack
    s.push(1);
    s.push(2);
    s.push(3);

    cout << "Stack before reverse: ";
    printStack(s);

    // Call the function to reverse the stack
    reverseStack(s);

    cout << "Stack after reverse: ";
    printStack(s);

    return 0;
}
