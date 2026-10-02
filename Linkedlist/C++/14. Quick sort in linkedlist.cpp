#include <iostream>
using namespace std;

// Node structure for the linked list
struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(nullptr) {}
};

// Partition function to partition the list around the pivot element
Node* partition(Node* head, Node* tail) {
    // Set the pivot as the head node
    Node* pivot = head;
    Node* prev = head;       // Tracks the end of the "smaller than pivot" section
    Node* cur = head->next;  // Starts just after the pivot

    // Traverse the list from head to tail to arrange elements around the pivot
    while (cur != tail->next) {
        // If the current node's data is less than the pivot's data, it should be moved to the "smaller" section
        if (cur->data < pivot->data) {
            // Move the node to the "smaller" section by swapping
            prev = prev->next;          // Move prev one step forward
            swap(prev->data, cur->data); // Swap values of prev->next and current node
        }
        cur = cur->next; // Move to the next node
    }
    
    // Move pivot to its final sorted position by swapping with prev
    swap(pivot->data, prev->data);
    return prev; // Return the final position of the pivot
}

// Recursive QuickSort function to sort the linked list
void quickSortRec(Node* head, Node* tail) {
    // Base condition: If the list is empty or has one element, it's already sorted
    if (head == tail || head == nullptr || tail == nullptr) return;

    // Partition the list and get the pivot node
    Node* pivot = partition(head, tail);

    // Recursively sort the left and right parts around the pivot
    quickSortRec(head, pivot);           // Left of pivot
    quickSortRec(pivot->next, tail);     // Right of pivot
}

// Function to start QuickSort on the list by finding the tail node
void quickSort(Node** headRef) {
    Node* tail = *headRef;
    // Traverse to the end of the list to find the tail node
    while (tail->next != nullptr) {
        tail = tail->next;
    }
    // Begin recursive quicksort from head to tail
    quickSortRec(*headRef, tail);
}

// Helper function to print the linked list
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

// Helper function to add a node to the end of the list
void appendNode(Node*& head, int value) {
    if (head == nullptr) {
        head = new Node(value);
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr) temp = temp->next;
    temp->next = new Node(value);
}

int main() {
    Node* head = nullptr;
    appendNode(head, 3);
    appendNode(head, 5);
    appendNode(head, 8);
    appendNode(head, 5);
    appendNode(head, 10);
    appendNode(head, 2);
    appendNode(head, 1);

    cout << "Original List: ";
    printList(head);

    quickSort(&head);

    cout << "Sorted List: ";
    printList(head);

    return 0;
}
/* 
Let’s walk through an example of how this `partition` function operates on a linked list. This example will illustrate how the function rearranges nodes around the pivot.

### Example

Suppose we have the following linked list:

```
Head -> 4 -> 1 -> 3 -> 9 -> 2 -> Tail
```

We'll choose the **head node (4)** as the pivot. We want to rearrange the list such that:
- All nodes with values less than `4` are to the left of the pivot.
- All nodes with values greater than or equal to `4` are to the right.

### Step-by-Step Walkthrough

1. **Initialization**:
   - `pivot` points to `4`.
   - `prev` starts at `4`, which is our initial pivot.
   - `cur` starts at the next node, which is `1`.

2. **First Iteration** (`cur` = `1`):
   - `1 < 4` (it's less than the pivot), so we need to move `1` into the "smaller" section.
   - `prev` moves to the next node (which is `1`), and we swap `prev` (`1`) with `cur` (`1`). Since `prev` and `cur` are the same node here, the list remains unchanged.
   - **List after this step**: `4 -> 1 -> 3 -> 9 -> 2`
   - `cur` moves to the next node, `3`.

3. **Second Iteration** (`cur` = `3`):
   - `3 < 4` (less than the pivot), so we need to move `3` into the "smaller" section.
   - `prev` moves to the next node (`3`), and we swap `prev` (`3`) with `cur` (`3`). Again, since `prev` and `cur` are the same, the list remains unchanged.
   - **List after this step**: `4 -> 1 -> 3 -> 9 -> 2`
   - `cur` moves to the next node, `9`.

4. **Third Iteration** (`cur` = `9`):
   - `9 >= 4` (not less than the pivot), so we do **not** move it into the "smaller" section.
   - We don't move `prev`.
   - **List after this step**: `4 -> 1 -> 3 -> 9 -> 2`
   - `cur` moves to the next node, `2`.

5. **Fourth Iteration** (`cur` = `2`):
   - `2 < 4` (less than the pivot), so we move `2` into the "smaller" section.
   - `prev` moves to the next node (`9`), and we swap `prev` (`9`) with `cur` (`2`).
   - **List after this step**: `4 -> 1 -> 3 -> 2 -> 9`
   - `cur` moves to `tail->next` (end of list).

6. **Placing the Pivot in Final Position**:
   - After the loop completes, `prev` points to `2`, which is the last node in the "smaller" section.
   - We swap `pivot` (`4`) with `prev` (`2`).
   - **Final List after Partitioning**: `2 -> 1 -> 3 -> 4 -> 9`

### Result

The final list after partitioning is:

```
2 -> 1 -> 3 -> 4 -> 9
```

Here:
- `4` is in its correct position.
- All elements to the left (`2`, `1`, `3`) are less than `4`.
- All elements to the right (`9`) are greater than or equal to `4`.

The `partition` function returns the node with value `4`, which is the final position of the pivot in this segment of the list.

*/