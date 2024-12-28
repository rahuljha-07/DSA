#include <iostream>
#include <vector>
using namespace std;

class MinHeap {
    vector<int> heap;

    // Recursive function to heapify a subtree rooted at index i
    void minHeapify(int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // Compare with left child
        if (left < heap.size() && heap[left] < heap[smallest])
            smallest = left;

        // Compare with right child
        if (right < heap.size() && heap[right] < heap[smallest])
            smallest = right;

        // If root is not smallest, swap with smallest and continue heapifying
        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            minHeapify(smallest);
        }
    }

public:
    MinHeap(const vector<int>& arr) {
        heap = arr;  // Copy the array into the heap
        int n = heap.size();

        // Perform bottom-up heap construction
        for (int i = n / 2 - 1; i >= 0; i--) {
            minHeapify(i);
        }
    }

    void insert(int val) {
        heap.push_back(val);
        int i = heap.size() - 1;

        // Up-heapify (bubble up)
        while (i != 0 && heap[(i - 1) / 2] > heap[i]) {
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void removeMin() {
        if (heap.empty()) return;

        heap[0] = heap.back();
        heap.pop_back();
        minHeapify(0);
    }

    int getMin() const {
        if (!heap.empty()) return heap[0];
        return -1;  // Indicate heap is empty
    }

    void printHeap() const {
        for (int val : heap) cout << val << " ";
        cout << endl;
    }
};

int main() {
    vector<int> arr = {40, 30, 15, 20, 10};
    MinHeap minHeap(arr);  // Build MinHeap from array

    cout << "MinHeap elements after building from array: ";
    minHeap.printHeap();

    cout << "Minimum element: " << minHeap.getMin() << endl;

    minHeap.removeMin();
    cout << "After removing minimum element: ";
    minHeap.printHeap();

    return 0;
}
