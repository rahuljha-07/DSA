class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Function to split the linked list into two halves using a slow and fast pointer approach.
def findmiddle(cur):
    slow = cur
    # Starting fast one node ahead ensures a two-node list actually splits.
    fast = cur.next
    # Move fast by 2 steps and slow by 1 step until fast reaches the end of the list.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Split the list at the middle point.
    first = cur
    second = slow.next
    # End the first half.
    slow.next = None
    return first, second


# Function to merge two sorted linked lists iteratively.
def mergeboth(first, second):
    # Initialize with a dummy value
    dummy = Node(0)
    tail = dummy
    while first and second:
        if first.data <= second.data:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next
    tail.next = first if first else second
    result = dummy.next
    return result


# Recursive function to perform merge sort on the linked list.
def mergesorting(head):
    cur = head
    if not cur or not cur.next:
        return head
    # Step 1: Split the list into two halves using findmiddle.
    first, second = findmiddle(cur)
    # Step 2: Sort each half.
    first = mergesorting(first)
    second = mergesorting(second)
    # Step 3: Merge the sorted halves.
    head = mergeboth(first, second)
    return head


def mergeSort(head):
    head = mergesorting(head)
    return head


'''
Let n be the number of nodes.
Time: O(n log n): splitting and merging together scan O(n) nodes per
recursion level. Halving each list gives O(log n) levels.
Space: O(log n) auxiliary: balanced recursive calls stay on the stack.
Merging is iterative, reuses input nodes, and needs one temporary dummy
node per active merge rather than an O(n) copied array.
'''
