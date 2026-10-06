class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to reverse a doubly linked list
def reverse(head):
    if head is None:
        return None
    curr = head
    temp = None
    # Swap next and prev pointers for each node
    while curr is not None:
        # Store the previous pointer
        temp = curr.prev
        # Swap next and prev
        curr.prev = curr.next
        # Complete the swap
        curr.next = temp
        # Update head to the current node
        head = curr
        # Move to the next node in original order
        curr = curr.prev
    # Return the new head of the reversed list
    return head


# Recursive function to reverse the linked list
def reverseRecursive(curr, revHead):
    if curr is None or curr.next is None:
        revHead[0] = curr
        if curr:
            curr.prev = None
        # Return last node (new tail)
        return curr
    # Recursive call to process the next node
    newHead = reverseRecursive(curr.next, revHead)
    # Link the current node to the reversed list
    newHead.next = curr
    curr.prev = newHead
    # Mark current node as the new tail
    curr.next = None
    # Return current node to help in backtracking
    return curr


# Distinct wrapper name preserves both C++ reverse alternatives.
def reverseUsingRecursion(head):
    # This will store the new head after reversal
    revHead = [None]
    reverseRecursive(head, revHead)
    # Update the head of the original list to the reversed list
    head = revHead[0]
    return head


'''
Let n be the number of nodes.
Time: O(n) for both approaches: each node's next/prev links change once.
Iterative space: O(1) auxiliary for curr/temp and head.
Recursive space: O(n) auxiliary because n calls wait on the stack;
revHead is a single-item reference holder, not a copied list of nodes.
Both methods reuse nodes and ensure the new head's prev is None.
'''
