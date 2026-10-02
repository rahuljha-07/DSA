#include <iostream>
#include <queue>

using namespace std;

// Function to interleave the first half with the second half of a queue
void interleaveQueue(queue<int>& q) {
    if (q.size() % 2 != 0) {
        cout << "Queue size must be even for interleaving.\n";
        return;
    }

    int n = q.size();
    int halfSize = n / 2;
    queue<int> firstHalf;

    // Step 1: Move the first half of elements to another queue
    for (int i = 0; i < halfSize; i++) {
        firstHalf.push(q.front());
        q.pop();
    }

    // Step 2: Interleave elements from firstHalf and secondHalf (remaining q elements)
    while (!firstHalf.empty()) {
        q.push(firstHalf.front());  // First half element
        firstHalf.pop();

        q.push(q.front());  // Second half element
        q.pop();
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
