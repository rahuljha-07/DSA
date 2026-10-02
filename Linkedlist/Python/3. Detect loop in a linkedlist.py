def detectCycle(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            return True
    return False


'''
Let n be the number of distinct reachable nodes.
Time: O(n): without a cycle, fast reaches the end; with a cycle, the
pointers meet within a linear number of steps (their gap shrinks each lap).
Space: O(1) auxiliary: only slow and fast pointers are stored.
'''
