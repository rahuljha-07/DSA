class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Partition function to partition the list around the pivot element
def partition(head, tail):
    # Set the pivot as the head node
    pivot = head
    # Tracks the end of the "smaller than pivot" section
    prev = head
    # Starts just after the pivot
    cur = head.next
    # Traverse the list from head to tail to arrange elements around the pivot
    while cur is not tail.next:
        if cur.data < pivot.data:
            # Move the node to the "smaller" section by swapping
            # Move prev one step forward
            prev = prev.next
            prev.data, cur.data = cur.data, prev.data
        # Move to the next node
        cur = cur.next
    # Move pivot to its final sorted position by swapping with prev
    pivot.data, prev.data = prev.data, pivot.data
    # Return the final position of the pivot
    return prev


# Recursive QuickSort function to sort the linked list
def quickSortRec(head, tail):
    if head is tail or head is None or tail is None:
        return
    # Partition the list and get the pivot node
    pivot = partition(head, tail)
    # Exclude the pivot so the left recursive range always gets smaller.
    if pivot is not head:
        prev = head
        while prev.next is not pivot:
            prev = prev.next
        # Recursively sort the left and right parts around the pivot
        # Left of pivot
        quickSortRec(head, prev)
    if pivot is not tail:
        # Right of pivot
        quickSortRec(pivot.next, tail)


# Function to start QuickSort on the list by finding the tail node
def quickSort(headRef):
    tail = headRef
    if tail is None:
        return headRef
    # Traverse to the end of the list to find the tail node
    while tail.next is not None:
        tail = tail.next
    # Begin recursive quicksort from head to tail
    quickSortRec(headRef, tail)
    return headRef


# Helper function to print the linked list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Helper function to add a node to the end of the list
def appendNode(head, value):
    if head is None:
        head = Node(value)
        return head
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(value)
    return head


def main():
    head = None
    head = appendNode(head, 3)
    head = appendNode(head, 5)
    head = appendNode(head, 8)
    head = appendNode(head, 5)
    head = appendNode(head, 10)
    head = appendNode(head, 2)
    head = appendNode(head, 1)
    print("Original List: ", end="")
    printList(head)
    head = quickSort(head)
    print("Sorted List: ", end="")
    printList(head)


if __name__ == "__main__":
    main()


'''
Let n be the number of nodes (complexities describe quickSort, not setup).
Time: O(n log n) average when pivots give reasonably balanced partitions:
partitioning and finding the pivot's predecessor cost O(n) per level.
Worst case O(n^2): head pivots on sorted or equal data can leave subproblems
of sizes n-1, n-2, ...; their traversal costs sum to O(n^2).
Space: O(log n) average, O(n) worst-case auxiliary recursion depth.
Data is swapped inside existing nodes; no result list is allocated.
The demo builds its list by repeated tail searches, costing O(n^2) setup.
'''
