def isCircular(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
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
