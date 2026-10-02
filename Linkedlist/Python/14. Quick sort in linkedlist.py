class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def partition(head, tail):
    pivot = head
    prev = head
    cur = head.next
    while cur is not tail.next:
        if cur.data < pivot.data:
            prev = prev.next
            prev.data, cur.data = cur.data, prev.data
        cur = cur.next
    pivot.data, prev.data = prev.data, pivot.data
    return prev


def quickSortRec(head, tail):
    if head is tail or head is None or tail is None:
        return
    pivot = partition(head, tail)
    # Exclude the pivot so the left recursive range always gets smaller.
    if pivot is not head:
        prev = head
        while prev.next is not pivot:
            prev = prev.next
        quickSortRec(head, prev)
    if pivot is not tail:
        quickSortRec(pivot.next, tail)


def quickSort(headRef):
    tail = headRef
    if tail is None:
        return headRef
    while tail.next is not None:
        tail = tail.next
    quickSortRec(headRef, tail)
    return headRef


def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


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
