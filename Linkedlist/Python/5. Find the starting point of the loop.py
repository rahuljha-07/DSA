def findLoopStart(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    hasCycle = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            hasCycle = True
            break
    if not hasCycle:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


'''
Let n be the number of distinct reachable nodes.
Time: O(n): Floyd's detection needs O(n) steps. Resetting slow to head
and advancing both pointers to the entry takes at most another O(n).
Space: O(1) auxiliary: only two pointers and a cycle flag are stored.
'''
