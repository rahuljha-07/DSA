#include <iostream>
using namespace std;

// Function to maintain the max heap property for a given subtree rooted at index 'i'
void heapify(int arr[], int n, int i) {
    if (i >= n) return;  // If index 'i' is out of bounds, return

    int largest = i;  // Assume the largest element is at the root of the subtree
    int l = 2 * i + 1;  // Left child index
    int r = 2 * i + 2;  // Right child index

    // If the left child exists and is greater than the root, update 'largest'
    if (l < n && arr[l] > arr[largest]) largest = l;

    // If the right child exists and is greater than the root (or left child), update 'largest'
    if (r < n && arr[r] > arr[largest]) largest = r;

    // If the root is not the largest, swap it with the largest and recursively heapify the affected subtree
    if (largest != i) {
        swap(arr[i], arr[largest]);  // Swap the root with the largest child
        heapify(arr, n, largest);    // Recursively apply heapify to the affected subtree
    }
}

// Function to build a max heap from an unsorted array
void buildheap(int arr[], int n) {
    int start = (n / 2) - 1;  // Start from the last non-leaf node (n/2 - 1)
    for (int i = start; i >= 0; i--) {
        heapify(arr, n, i);  // Apply heapify to each node starting from the last non-leaf node
    }
}

// Function to merge two heaps into one heap
void mergeHeaps(int merged[], int a[], int b[], int n, int m) {
    // Copy elements of heap 'a' into the 'merged' array
    for (int i = 0; i < n; i++) merged[i] = a[i];

    // Copy elements of heap 'b' into the 'merged' array starting from index 'n'
    for (int i = 0; i < m; i++) merged[n + i] = b[i];

    // Build a max heap from the 'merged' array (after combining both heaps)
    buildheap(merged, n + m);
}

// Main function to test the heap merging functionality
int main() {
    int a[] = {10, 5, 6, 2};  // First heap (unsorted array)
    int b[] = {8, 7, 3, 4};   // Second heap (unsorted array)

    int n = sizeof(a) / sizeof(a[0]);  // Size of the first heap (array 'a')
    int m = sizeof(b) / sizeof(b[0]);  // Size of the second heap (array 'b')

    int merged[n + m];  // Array to store the merged heap

    // Call the mergeHeaps function to merge both heaps into the 'merged' array
    mergeHeaps(merged, a, b, n, m);

    // Output the merged heap array
    cout << "Merged heap: ";
    for (int i = 0; i < n + m; i++) {
        cout << merged[i] << " ";  // Print each element in the merged heap
    }
    cout << endl;

    return 0;
}
