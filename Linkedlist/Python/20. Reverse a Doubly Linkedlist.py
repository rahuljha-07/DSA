class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def reverse(head):
    if head is None:
        return None
    curr = head
    temp = None
    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        head = curr
        curr = curr.prev
    return head


def reverseRecursive(curr, revHead):
    if curr is None or curr.next is None:
        revHead[0] = curr
        if curr:
            curr.prev = None
        return curr
    newHead = reverseRecursive(curr.next, revHead)
    newHead.next = curr
    curr.prev = newHead
    curr.next = None
    return curr


# Distinct wrapper name preserves both C++ reverse alternatives.
def reverseUsingRecursion(head):
    revHead = [None]
    reverseRecursive(head, revHead)
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
