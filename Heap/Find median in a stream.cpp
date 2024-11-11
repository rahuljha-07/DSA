#include <iostream>
#include <queue>
using namespace std;

class MedianFinder {
private:
    // Min heap to store the larger half of the stream
    priority_queue<int, vector<int>, greater<int>> r;  // right half (min-heap)
    // Max heap to store the smaller half of the stream
    priority_queue<int> l;  // left half (max-heap)

public:
    // Function to insert a new number into the heaps
    void insertHeap(int x) {
        // If the new number is larger than the top of the right half (min-heap), it belongs to the right half
        if (!r.empty() && x > r.top()) {
            r.push(x);
        } else {
            // Otherwise, it belongs to the left half (max-heap)
            l.push(x);
        }

        // Balance the heaps if their sizes differ by more than 1
        balanceHeaps();
    }

    // Function to balance the two heaps (left max-heap and right min-heap)
    void balanceHeaps() {
        // If the left heap has more than 1 extra element, move the top element to the right heap
        if (l.size() - r.size() == 2) {
            r.push(l.top());
            l.pop();
        }
        // If the right heap has more than 1 extra element, move the top element to the left heap
        else if (r.size() - l.size() == 2) {
            l.push(r.top());
            r.pop();
        }
    }

    // Function to return the median of the current numbers
    double getMedian() {
        // If both heaps are empty, return -1 (this should not happen in normal usage)
        if (l.empty() && r.empty()) return -1;

        // If the left heap has more elements, the median is the top of the left heap (max-heap)
        if (l.size() > r.size()) {
            return l.top();
        }
        // If the right heap has more elements, the median is the top of the right heap (min-heap)
        else if (r.size() > l.size()) {
            return r.top();
        }
        // If both heaps are of the same size, the median is the average of the tops of both heaps
        else {
            return (l.top() + r.top()) / 2.0;  // Return as float/double
        }
    }
};

int main() {
    MedianFinder finder;
    finder.insertHeap(1);
    cout << "Median after inserting 1: " << finder.getMedian() << endl;  // Output: 1

    finder.insertHeap(2);
    cout << "Median after inserting 2: " << finder.getMedian() << endl;  // Output: 1.5

    finder.insertHeap(3);
    cout << "Median after inserting 3: " << finder.getMedian() << endl;  // Output: 2

    return 0;
}
