#include <iostream>
#include <vector>

using namespace std;

class CircularQueue {
private:
    vector<int> data;
    int front;
    int rear;
    int capacity;

public:
    // Constructor to initialize the circular queue with a fixed size
    CircularQueue(int size) : data(size), front(-1), rear(-1), capacity(size) {}

    // Check if the queue is empty
    bool isEmpty() {
        return front == -1;
    }

    // Check if the queue is full
    bool isFull() {
        return (rear + 1) % capacity == front;
    }

    // Enqueue an element into the circular queue
    bool enqueue(int value) {
        if (isFull()) {
            cout << "Queue Overflow\n";
            return false;
        }
        if (isEmpty()) {
            front = 0;
        }
        rear = (rear + 1) % capacity;
        data[rear] = value;
        return true;
    }

    // Dequeue an element from the circular queue
    bool dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return false;
        }
        if (front == rear) {
            // Queue becomes empty after this dequeue
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % capacity;
        }
        return true;
    }

    // Get the front element of the queue
    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return data[front];
    }

    // Get the rear element of the queue
    int getRear() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return data[rear];
    }
};

// Example usage
int main() {
    CircularQueue queue(5);  // Initialize a circular queue of capacity 5

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    queue.enqueue(40);
    queue.enqueue(50);

    cout << "Front element: " << queue.getFront() << endl;  // Should print 10
    cout << "Rear element: " << queue.getRear() << endl;    // Should print 50

    queue.dequeue();
    cout << "After one dequeue, front element: " << queue.getFront() << endl;  // Should print 20

    queue.enqueue(60);
    cout << "After enqueue 60, rear element: " << queue.getRear() << endl;    // Should print 60

    return 0;
}

//using doubly linklist
#include <iostream>

using namespace std;

// Node structure for doubly linked list
struct Node {
    int data;
    Node* next;
    Node* prev;

    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

class CircularQueue {
private:
    Node* front;
    Node* rear;

public:
    // Constructor to initialize an empty circular queue
    CircularQueue() : front(nullptr), rear(nullptr) {}

    // Destructor to clean up the linked list
    ~CircularQueue() {
        while (!isEmpty()) {
            dequeue();
        }
    }

    // Check if the queue is empty
    bool isEmpty() {
        return front == nullptr;
    }

    // Enqueue an element into the circular queue
    void enqueue(int value) {
        Node* newNode = new Node(value);
        if (isEmpty()) {
            front = newNode;
            rear = newNode;
            front->next = rear; // Point front to rear
            front->prev = rear; // Point rear to front
            rear->next = front; // Make it circular
            rear->prev = front; // Make it circular
        } else {
            rear->next = newNode; // Link the new node after rear
            newNode->prev = rear; // Link back to rear
            newNode->next = front; // Circular link to front
            front->prev = newNode; // Circular link from front
            rear = newNode; // Move rear to the new node
        }
    }

    // Dequeue an element from the circular queue
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return;
        }

        Node* temp = front;
        if (front == rear) {
            // Only one element in the queue
            front = nullptr;
            rear = nullptr;
        } else {
            // Move front to the next node
            front = front->next;
            rear->next = front; // Maintain circularity
            front->prev = rear; // Maintain circularity
        }
        delete temp; // Free the memory of the dequeued node
    }

    // Get the front element of the queue
    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return front->data;
    }

    // Get the rear element of the queue
    int getRear() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return -1;
        }
        return rear->data;
    }

    // Print the elements of the queue (for demonstration)
    void printQueue() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return;
        }
        Node* current = front;
        do {
            cout << current->data << " ";
            current = current->next;
        } while (current != front);
        cout << endl;
    }
};

// Example usage
int main() {
    CircularQueue queue;

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    queue.enqueue(40);
    
    cout << "Queue after enqueuing: ";
    queue.printQueue(); // Should print 10 20 30 40

    cout << "Front element: " << queue.getFront() << endl; // Should print 10
    cout << "Rear element: " << queue.getRear() << endl;   // Should print 40

    queue.dequeue();
    cout << "After one dequeue, front element: " << queue.getFront() << endl; // Should print 20

    queue.enqueue(50);
    cout << "After enqueue 50, queue: ";
    queue.printQueue(); // Should print 20 30 40 50

    return 0;
}
