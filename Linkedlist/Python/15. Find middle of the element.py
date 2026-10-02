def findMiddle(head):
    if head is None:
        return -1
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data


'''
Let n be the number of nodes.
Time: O(n): fast crosses the list in about n/2 iterations, while slow
moves one node per iteration. For even n, it returns the second middle.
Space: O(1) auxiliary: only slow and fast pointers are stored.
'''
