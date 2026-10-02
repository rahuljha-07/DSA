class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverseIterative(head):
    prev = None
    current = head
    next = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reverseRecursive(head):
    if head is None or head.next is None:
        return head
    newHead = reverseRecursive(head.next)
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
