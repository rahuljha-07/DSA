#include <iostream>
#include <vector>
#include <unordered_map>
#include <deque>  // Using deque for O(1) dequeue operation

using namespace std;

class NQueuesInArray {
private:
    vector<int> vec;                 // Array to store the elements of all queues
    vector<int> free_indices;        // Indices in vec that are free for enqueueing
    unordered_map<int, deque<int>> queue_map;  // Map each queue to its indices in vec (deque for O(1) front removal)

public:
    // Constructor initializes the vector and free_indices
    NQueuesInArray(int size) {
        vec.resize(size, -1);  // Initialize the array with -1
        for (int i = 0; i < size; ++i) {
            free_indices.push_back(i);  // Initially, all indices are free
        }
    }

    // Enqueue a value in the specified queue
    void enqueue(int queue_num, int value) {
        if (free_indices.empty()) {
            cout << "Queue Overflow\n";
            return;
        }

        // Get an available index from free_indices
        int index = free_indices.back();
        free_indices.pop_back();

        // Place the value in vec and record the index in queue_map
        vec[index] = value;
        queue_map[queue_num].push_back(index);  // Using deque for O(1) enqueue at back
    }

    // Dequeue a value from the specified queue
    int dequeue(int queue_num) {
        if (queue_map.find(queue_num) == queue_map.end() || queue_map[queue_num].empty()) {
            cout << "Queue Underflow\n";
            return -1;
        }

        // Get the first index for this queue
        int front_index = queue_map[queue_num].front();  // O(1)
        queue_map[queue_num].pop_front();  // O(1) with deque

        // Retrieve the value at this index
        int value = vec[front_index];
        vec[front_index] = -1;  // Optional: reset the value

        // Mark this index as free
        free_indices.push_back(front_index);

        return value;
    }

    // Get the front value of the specified queue
    int front(int queue_num) {
        if (queue_map.find(queue_num) == queue_map.end() || queue_map[queue_num].empty()) {
            cout << "Queue is Empty\n";
            return -1;
        }

        // Get the first index for this queue
        int front_index = queue_map[queue_num].front();  // O(1)
        return vec[front_index];
    }
};

// Example usage
int main() {
    NQueuesInArray queues(10);  // Create an instance with a fixed-size array of 10

    queues.enqueue(1, 10);            // Enqueue 10 to queue 1
    queues.enqueue(2, 20);            // Enqueue 20 to queue 2
    queues.enqueue(1, 15);            // Enqueue 15 to queue 1

    cout << "Front of queue 1: " << queues.front(1) << endl;  // Should output 10
    cout << "Dequeued from queue 1: " << queues.dequeue(1) << endl;  // Should output 10
    cout << "Front of queue 1: " << queues.front(1) << endl;  // Should output 15
    cout << "Dequeued from queue 2: " << queues.dequeue(2) << endl;  // Should output 20
    cout << "Dequeued from queue 2: " << queues.dequeue(2) << endl;  // Should show "Queue Underflow"

    return 0;
}
