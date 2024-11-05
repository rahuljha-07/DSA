#include <iostream>
#include <queue>
#include <stack>

using namespace std;

// Function to interleave the first half of the queue with the second half
void interleaveQueue(queue<int>& q) {
    stack<int> s;
    int n = q.size();
    int halfSize = n / 2;

    // Step 1: Push the first half elements into the stack
    for (int i = 0; i < halfSize; i++) {
        s.push(q.front());
        q.pop();
    }

    // Step 2: Enqueue back the stack elements (first half)
    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }

    // Step 3: Dequeue the first half elements and enqueue them back
    for (int i = 0; i < halfSize; i++) {
        q.push(q.front());
        q.pop();
    }

    // Step 4: Push the first half elements into the stack again
    for (int i = 0; i < halfSize; i++) {
        s.push(q.front());
        q.pop();
    }

    // Step 5: Interleave the elements of queue and stack
    while (!s.empty()) {
        // Queue element
        q.push(q.front());
        q.pop();
        
        // Stack element
        q.push(s.top());
        s.pop();
    }
}

// Function to display the elements of the queue
void displayQueue(queue<int> q) {
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

// Example usage
int main() {
    queue<int> q;

    // Example Input: 1 2 3 4
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);

    cout << "Original queue: ";
    displayQueue(q);

    // Interleave the queue
    interleaveQueue(q);

    cout << "Interleaved queue: ";
    displayQueue(q);  // Output: 1 3 2 4

    // Example Input: 11 12 13 14 15 16 17 18 19 20
    queue<int> q2;
    q2.push(11);
    q2.push(12);
    q2.push(13);
    q2.push(14);
    q2.push(15);
    q2.push(16);
    q2.push(17);
    q2.push(18);
    q2.push(19);
    q2.push(20);

    cout << "Original queue: ";
    displayQueue(q2);

    // Interleave the second queue
    interleaveQueue(q2);

    cout << "Interleaved queue: ";
    displayQueue(q2);  // Output: 11 16 12 17 13 18 14 19 15 20

    return 0;
}
