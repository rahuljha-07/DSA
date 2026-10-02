#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> heap;

    // Recursive function to heapify a subtree rooted at index i
    void maxHeapify(int i) {
        int largest = i;
        int left = 2 * i + 1;  // Left child
        int right = 2 * i + 2; // Right child

        // If left child is larger than root
        if (left < heap.size() && heap[left] > heap[largest])
            largest = left;

        // If right child is larger than largest so far
        if (right < heap.size() && heap[right] > heap[largest])
            largest = right;

        // If largest is not root
        if (largest != i) {
            swap(heap[i], heap[largest]);
            // Recursively heapify the affected subtree
            maxHeapify(largest);
        }
    }

public:
    // Insert a new element into the heap
    void insert(int val) {
        heap.push_back(val); // Add the new element to the end of the heap
        int i = heap.size() - 1;

        // Up-heapify (bubble up) to maintain the heap property
        while (i != 0 && heap[(i - 1) / 2] < heap[i]) {
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    // Remove the maximum element (root of the heap)
    void removeMax() {
        if (heap.empty()) {
            cout << "Heap is empty!" << endl;
            return;
        }

        // Move the last element to the root and remove the last element
        heap[0] = heap.back();
        heap.pop_back();

        // Heapify the root to restore the heap property
        maxHeapify(0);
    }

    // Get the maximum element in the heap
    int getMax() const {
        if (!heap.empty()) return heap[0];
        return -1;  // Indicate that the heap is empty
    }

    // Print all elements in the heap
    void printHeap() const {
        for (int val : heap) cout << val << " ";
        cout << endl;
    }
};

int main() {
    MaxHeap maxHeap;

    maxHeap.insert(10);
    maxHeap.insert(20);
    maxHeap.insert(15);
    maxHeap.insert(30);
    maxHeap.insert(40);

    cout << "MaxHeap elements: ";
    maxHeap.printHeap();

    cout << "Maximum element: " << maxHeap.getMax() << endl;

    maxHeap.removeMax();
    cout << "After removing maximum element: ";
    maxHeap.printHeap();

    return 0;
}
