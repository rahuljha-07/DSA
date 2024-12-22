#include <iostream>
#include <queue>
#include <stack>

using namespace std;

// Function to reverse the first k elements of a queue
queue<int> modifyQueue(queue<int> q, int k) {
    stack<int> s;

    // Step 1: Push the first k elements into the stack
    for (int i = 0; i < k; i++) {
        s.push(q.front());  // Push the front element onto the stack
        q.pop();            // Remove the front element from the queue
    }

    // Step 2: Pop from the stack and enqueue back to the queue
    while (!s.empty()) {
        q.push(s.top());    // Push the top element from the stack to the queue
        s.pop();            // Remove the top element from the stack
    }

    // Step 3: Move the remaining elements (n - k) to the back of the queue
    int n = q.size();      // Get the current size of the queue
    for (int i = 0; i < n - k; i++) {
        q.push(q.front()); // Move the front element to the back
        q.pop();           // Remove the front element
    }

    return q; // Return the modified queue
}

// Example usage
int main() {
    queue<int> q;
    // Enqueue some elements
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);

    int k = 3; // Number of elements to reverse

    cout << "Original queue: ";
    for (int i = 0; i < 5; i++) {
        cout << q.front() << " "; // Display original queue
        q.pop();
    }
    cout << endl;

    // Reinitialize the queue
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);

    // Modify the queue
    q = modifyQueue(q, k);

    cout << "Modified queue after reversing first " << k << " elements: ";
    while (!q.empty()) {
        cout << q.front() << " "; // Display modified queue
        q.pop();
    }
    cout << endl;

    return 0;
}
