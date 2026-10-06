class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverseIterative(head):
    prev = None
    current = head
    next = None
    while current is not None:
        # Save the next node
        next = current.next
        # Reverse the link
        current.next = prev
        # Move prev up
        prev = current
        # Move current up
        current = next
    # New head of the reversed list
    return prev


def reverseRecursive(head):
    if head is None or head.next is None:
        return head
    # Reverse the rest of the list
    newHead = reverseRecursive(head.next)
    # Reverse the link for current node
    head.next.next = head
    head.next = None
    return newHead


'''
Let n be the number of nodes.
Time: O(n) for both methods because each node's link is reversed once.
Space: O(1) auxiliary for reverseIterative: only three pointers are used.
reverseRecursive uses O(n) auxiliary space: one call remains on the stack
for each node until recursion reaches the tail. No new list is created.
'''
