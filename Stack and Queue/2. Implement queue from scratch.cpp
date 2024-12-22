#include <iostream>
#include <vector>

using namespace std; // Using the standard namespace

class Queue {
private:
    vector<int> data; // Container to hold queue elements

public:
    // Enqueue operation to add an element at the rear of the queue
    void enqueue(int value) {
        data.push_back(value); // Add element to the end of the vector
    }

    // Dequeue operation to remove an element from the front of the queue
    void dequeue() {
        if (isEmpty()) {
            cerr << "Queue is empty, cannot dequeue." << endl;
            return;
        }
        data.erase(data.begin()); // Remove the first element from the vector
    }

    // Get the front element of the queue
    int getFront() {
        if (!isEmpty()) {
            return data.front(); // Return the first element
        } else {
            cerr << "Queue is empty, cannot access front." << endl;
            return -1; // or throw an exception
        }
    }

    // Check if the queue is empty
    bool isEmpty() {
        return data.empty(); // Queue is empty if the vector is empty
    }

    // Get the current size of the queue
    size_t size() {
        return data.size(); // Return the number of elements in the vector
    }
};

int main() {
    Queue queue;

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);

    cout << "Front element: " << queue.getFront() << endl; // Outputs: 10
    queue.dequeue();
    cout << "Front element after dequeue: " << queue.getFront() << endl; // Outputs: 20

    queue.dequeue();
    queue.dequeue();
    queue.dequeue(); // Attempting to dequeue from an empty queue

    return 0;
}
