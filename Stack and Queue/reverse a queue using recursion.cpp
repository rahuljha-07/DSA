#include <iostream>
#include <queue>

using namespace std;

// Function to print the elements of the queue (for demonstration)
void printQueue(queue<int> q) {
    // Print each element and remove it from the queue
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

// Recursive function to reverse the queue
void performReverse(queue<int>& q) {
    // Base case: If the queue is empty, return
    if (q.empty()) {
        return;
    }

    // Recursive case: Remove the front element
    int frontElement = q.front();
    q.pop();

    // Recursive call to reverse the remaining queue
    performReverse(q);

    // Add the removed element to the rear of the queue
    q.push(frontElement);
}

// Function to reverse the queue using recursion
void reverseQueue(queue<int>& q) {
    performReverse(q);
}

// Example usage
int main() {
    queue<int> q;

    // Enqueue some elements into the queue
    q.push(1);
    q.push(2);
    q.push(3);

    cout << "Queue before reverse: ";
    printQueue(q);
    
    // Call the function to reverse the queue
    reverseQueue(q);
    
    cout << "Queue after reverse: ";
    printQueue(q);

    return 0;
}
