#include <iostream>
#include <stack>

using namespace std;

// Function to print the elements of the stack (for demonstration)
void printStack(stack<int> s) {
    // Print each element and pop it from the stack
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

// Recursive function to reverse the stack
void performReverse(stack<int>& s) {
    // Base case: If the stack is empty, return
    if (s.empty()) {
        return;
    }

    // Recursive case: Pop the top element
    int topElement = s.top();
    s.pop();

    // Recursive call to reverse the remaining stack
    performReverse(s);

    // Push the popped element back onto the stack
    s.push(topElement);
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
