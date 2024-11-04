#include <iostream>
#include <stack>
#include <limits>

using namespace std;

class MinStack {
private:
    stack<int> s;            // Stack to hold the actual elements
    int minElement;          // Variable to track the minimum element

public:
    // Push function to add an element to the stack
    void push(int x) {
        // If the stack is empty, set minElement to the new element
        if (s.empty()) {
            s.push(x);
            minElement = x;  // Initialize minElement
        } else {
            // If the new element is less than or equal to the current min,
            // push a modified value to track the new minimum.
            if (x < minElement) {
                s.push(2 * x - minElement);  // Store a value that can help recover the new min
                minElement = x;               // Update the minElement
            } else {
                s.push(x);                    // Just push the new element
            }
        }
    }

    // Pop function to remove the top element from the stack
    void pop() {
        if (s.empty()) {
            cout << "Stack Underflow\n";    // Handle underflow condition
            return;
        }

        int topValue = s.top();
        s.pop();  // Remove the top element

        // If the popped value is less than the current minElement,
        // it means we are removing the minimum value.
        if (topValue < minElement) {
            minElement = 2 * minElement - topValue;  // Recover the previous minElement
        }
    }

    // Function to get the current top element of the stack
    int top() {
        if (s.empty()) {
            cout << "Stack is empty\n";
            return -1;  // Stack is empty
        }

        int topValue = s.top();
        // If topValue is less than the current minElement,
        // it indicates that this was a special value to track the minimum.
        return (topValue < minElement) ? minElement : topValue;
    }

    // Function to get the minimum element in the stack
    int getMin() {
        if (s.empty()) {
            cout << "Stack is empty\n";
            return -1;  // Stack is empty
        }
        return minElement;  // Return the minimum element
    }
};

// Example usage
int main() {
    MinStack minStack;

    minStack.push(5);
    cout << "Current Min: " << minStack.getMin() << endl; // Should return 5

    minStack.push(3);
    cout << "Current Min: " << minStack.getMin() << endl; // Should return 3

    minStack.push(7);
    cout << "Current Min: " << minStack.getMin() << endl; // Should return 3

    minStack.pop();
    cout << "Current Min: " << minStack.getMin() << endl; // Should return 3

    minStack.pop();
    cout << "Current Min: " << minStack.getMin() << endl; // Should return 5

    return 0;
}
