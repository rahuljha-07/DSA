def removeLoop(head):
    if head is None or head.next is None:
        return
    slow = head
    fast = head
    hasCycle = False
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            hasCycle = True
            break
    if not hasCycle:
        return
    slow = head
    if slow is fast:
        while fast.next is not slow:
            fast = fast.next
    else:
        while slow.next is not fast.next:
            slow = slow.next
            fast = fast.next
    fast.next = None


'''
Let n be the number of distinct reachable nodes.
Time: O(n): cycle detection takes O(n), then locating the predecessor
of the loop's entry takes at most another O(n). Adding passes stays O(n).
Space: O(1) auxiliary: only pointers and a boolean are used; the loop
is removed by changing one existing next link.
'''
