def isCircular(head):
    # If the list is empty, it's not circular
    if head is None:
        return False
    # Initialize slow and fast pointers
    slow = head
    fast = head
    # Traverse the list
    while fast is not None and fast.next is not None:
        # Move slow pointer one step
        slow = slow.next
        # Move fast pointer two steps
        fast = fast.next.next
        if slow is fast:
            return True
    return False


'''
Let n be the number of distinct reachable nodes.
Time: O(n): fast either reaches None or catches slow inside a cycle within
O(n) steps. Space: O(1) auxiliary: only two pointers are stored.
Like the C++ source, this detects any cycle, not just a cycle back to head.
'''
