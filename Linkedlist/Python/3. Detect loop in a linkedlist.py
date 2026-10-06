def detectCycle(head):
    # If the list is empty, there's no cycle
    if head is None:
        return False
    # Initialize two pointers
    slow = head
    fast = head
    # Loop to move the pointers through the list
    while fast.next and fast.next.next:
        # Move the fast pointer two steps and slow pointer one step
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            return True
    # If the loop ends, no cycle was found
    return False


'''
Let n be the number of distinct reachable nodes.
Time: O(n): without a cycle, fast reaches the end; with a cycle, the
pointers meet within a linear number of steps (their gap shrinks each lap).
Space: O(1) auxiliary: only slow and fast pointers are stored.
'''
