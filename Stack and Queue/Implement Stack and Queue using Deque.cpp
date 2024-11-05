#include <iostream>
#include <deque>

using namespace std;

// Stack implementation using deque
class Stack {
private:
    deque<int> dq;  // Deque to store elements

public:
    // Push an element onto the stack
    void push(int value) {
        dq.push_back(value);  // Insert at the back
    }

    // Pop the top element from the stack
    void pop() {
        if (dq.empty()) {
            cout << "Stack Underflow\n";
            return;
        }
        dq.pop_back();  // Remove from the back
    }

    // Get the top element of the stack
    int top() {
        if (dq.empty()) {
            cout << "Stack is empty\n";
            return -1;
        }
        return dq.back();  // Return the last element
    }

    // Check if the stack is empty
    bool empty() {
        return dq.empty();
    }
};

// Queue implementation using deque
class Queue {
private:
    deque<int> dq;  // Deque to store elements

public:
    // Enqueue an element into the queue
    void enqueue(int value) {
        dq.push_back(value);  // Insert at the back
    }

    // Dequeue the front element from the queue
    void dequeue() {
        if (dq.empty()) {
            cout << "Queue Underflow\n";
            return;
        }
        dq.pop_front();  // Remove from the front
    }

    // Get the front element of the queue
    int front() {
        if (dq.empty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return dq.front();  // Return the first element
    }

    // Check if the queue is empty
    bool empty() {
        return dq.empty();
    }
};

// Example usage
int main() {
    Stack stack;
    stack.push(10);
    stack.push(20);
    cout << "Top of stack: " << stack.top() << endl;  // Should print 20
    stack.pop();
    cout << "Top of stack after pop: " << stack.top() << endl;  // Should print 10

    Queue queue;
    queue.enqueue(30);
    queue.enqueue(40);
    cout << "Front of queue: " << queue.front() << endl;  // Should print 30
    queue.dequeue();
    cout << "Front of queue after dequeue: " << queue.front() << endl;  // Should print 40

    return 0;
}
