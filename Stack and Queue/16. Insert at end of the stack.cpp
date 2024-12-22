#include <iostream>
#include <stack>

using namespace std;

// Recursive function to insert a value at the end of a stack
void insertAtEndStack(stack<int>& s, int val) {
    // Base case: If the stack is empty, push the value
    if (s.empty()) {
        s.push(val);
        return;
    }

    // Recursive case: Pop the top element
    int topElement = s.top();
    s.pop();

    // Recursive call to insert the value into the remaining stack
    insertAtEndStack(s, val);

    // Push the popped element back onto the stack
    s.push(topElement);
}

// Function to perform the insertion of a value into the stack
void performInsertion(stack<int>& s, int val) {
    // Insert value at the end of the stack
    insertAtEndStack(s, val);
}

// Function to print the elements of the stack (for demonstration)
void printStack(stack<int> s) {
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}


// Example usage
int main() {
    stack<int> s;

    // Pushing some elements onto the stack
    s.push(1);
    s.push(2);
    s.push(3);

    cout << "Stack before insertion: ";
    printStack(s);
    
    // Call the function to perform the stack insertion
    performInsertion(s, 4);
    
    cout << "Stack after inserting 4 at the end: ";
    printStack(s);

    return 0;
}
