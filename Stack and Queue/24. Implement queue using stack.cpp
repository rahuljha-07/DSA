#include <iostream>
#include <stack>

using namespace std;

class QueueUsingStacks {
private:
    stack<int> input;  // Stack to handle enqueue operations
    stack<int> output; // Stack to handle dequeue operations

public:
    // Enqueue an element into the queue
    void enqueue(int value) {
        input.push(value);
    }

    // Dequeue an element from the queue
    int dequeue() {
        if (output.empty()) {
            if (input.empty()) {
                cout << "Queue Underflow\n";
                return -1;
            }
            // Transfer all elements from input stack to output stack
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        // Pop from output stack, which represents the front of the queue
        int front = output.top();
        output.pop();
        return front;
    }

    // Get the front element of the queue
    int front() {
        if (output.empty()) {
            if (input.empty()) {
                cout << "Queue is Empty\n";
                return -1;
            }
            // Transfer all elements from input stack to output stack
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();  // Front of the queue is the top of output stack
    }

    // Check if the queue is empty
    bool empty() {
        return input.empty() && output.empty();
    }
};

// Example usage
int main() {
    QueueUsingStacks queue;
    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);

    cout << "Front of queue: " << queue.front() << endl;  // Should print 10
    cout << "Dequeued: " << queue.dequeue() << endl;       // Should print 10
    cout << "Front of queue: " << queue.front() << endl;   // Should print 20
    cout << "Dequeued: " << queue.dequeue() << endl;       // Should print 20

    queue.enqueue(40);
    cout << "Front of queue: " << queue.front() << endl;   // Should print 30
    cout << "Dequeued: " << queue.dequeue() << endl;       // Should print 30
    cout << "Dequeued: " << queue.dequeue() << endl;       // Should print 40

    if (queue.empty()) {
        cout << "Queue is empty\n";
    }

    return 0;
}
