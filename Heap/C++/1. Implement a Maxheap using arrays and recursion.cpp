#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> heap;

    // Recursive function to heapify a subtree rooted at index i
    void maxHeapify(int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // Compare with left child
        if (left < heap.size() && heap[left] > heap[largest])
            largest = left;

        // Compare with right child
        if (right < heap.size() && heap[right] > heap[largest])
            largest = right;

        // If root is not largest, swap with largest and continue heapifying
        if (largest != i) {
            swap(heap[i], heap[largest]);
            maxHeapify(largest);
        }
    }

public:
    MaxHeap(const vector<int>& arr) {
        heap = arr; // Copy the array into the heap
        int n = heap.size();

        // Perform bottom-up heap construction
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapify(i);
        }
    }

    void insert(int val) {
        heap.push_back(val);
        int i = heap.size() - 1;

        // Up-heapify (bubble up)
        while (i != 0 && heap[(i - 1) / 2] < heap[i]) {
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void removeMax() {
        if (heap.empty()) return;
        
        heap[0] = heap.back();
        heap.pop_back();
        maxHeapify(0);
    }

    int getMax() const {
        if (!heap.empty()) return heap[0];
        return -1;  // Indicate heap is empty
    }

    void printHeap() const {
        for (int val : heap) cout << val << " ";
        cout << endl;
    }
};

int main() {
    vector<int> arr = {10, 20, 15, 30, 40};
    MaxHeap maxHeap(arr);  // Build MaxHeap from array

    cout << "MaxHeap elements after building from array: ";
    maxHeap.printHeap();

    cout << "Maximum element: " << maxHeap.getMax() << endl;

    maxHeap.removeMax();
    cout << "After removing maximum element: ";
    maxHeap.printHeap();

    return 0;
}
