#include <iostream>
#include <vector>

using namespace std; // Using the standard namespace

class Stack {
private:
    vector<int> data; // Container to hold stack elements

public:
    // Push an element onto the stack
    void push(int value) {
        data.push_back(value);
    }

    // Remove the top element from the stack
    void pop() {
        if (!isEmpty()) {
            data.pop_back();
        } else {
            cerr << "Stack is empty, cannot pop." << endl;
        }
    }

    // Get the top element of the stack
    int top() {
        if (!isEmpty()) {
            return data.back();
        } else {
            cerr << "Stack is empty, cannot access top." << endl;
            return -1; // or throw an exception
        }
    }

    // Check if the stack is empty
    bool isEmpty() {
        return data.empty();
    }

    // Get the current size of the stack
    size_t size() {
        return data.size();
    }
};

int main() {
    Stack stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << "Top element: " << stack.top() << endl; // Outputs: 30
    stack.pop();
    cout << "Top element after pop: " << stack.top() << endl; // Outputs: 20

    stack.pop();
    stack.pop();
    stack.pop(); // Attempting to pop from an empty stack

    return 0;
}
