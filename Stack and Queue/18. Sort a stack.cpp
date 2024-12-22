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

// Recursive function to insert an element in sorted order into a stack
void sortedInsert(stack<int>& s, int element) {
    // Base case: If the stack is empty or the top element is less than or equal to the element
    if (s.empty() || s.top() <= element) {
        s.push(element);
        return;
    }

    // Recursive case: Pop the top element and store it
    int topElement = s.top();
    s.pop();

    // Recursive call to insert the element in the remaining stack
    sortedInsert(s, element);

    // Push the popped element back onto the stack
    s.push(topElement);
}

// Recursive function to sort the stack
void sortStack(stack<int>& s) {
    // Base case: If the stack is empty, return
    if (s.empty()) {
        return;
    }

    // Recursive case: Pop the top element
    int topElement = s.top();
    s.pop();

    // Recursive call to sort the remaining stack
    sortStack(s);

    // Insert the popped element in sorted order
    sortedInsert(s, topElement);
}

// Example usage
int main() {
    stack<int> s;

    // Pushing some elements onto the stack
    s.push(3);
    s.push(1);
    s.push(4);
    s.push(2);

    cout << "Stack before sorting: ";
    printStack(s);
    
    // Call the function to sort the stack
    sortStack(s);
    
    cout << "Stack after sorting: ";
    printStack(s);

    return 0;
}
