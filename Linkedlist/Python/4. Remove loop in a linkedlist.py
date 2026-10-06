# Function to detect and remove the loop in the linked list
def removeLoop(head):
    if head is None or head.next is None:
        return
    slow = head
    fast = head
    # Step 1: Detect if there's a cycle in the list
    hasCycle = False
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            hasCycle = True
            break
    # If there's no cycle, return as there's nothing to remove
    if not hasCycle:
        return
    # Step 2: Find the starting point of the loop
    # Reset slow to the head of the list
    slow = head
    if slow is fast:
        # Special case: If the cycle starts at the head of the list
        # Move both pointers one step at a time until they meet at the start of the loop
        while fast.next is not slow:
            fast = fast.next
    else:
        while slow.next is not fast.next:
            slow = slow.next
            fast = fast.next
    # Step 3: Remove the loop by setting the next of the last node in the loop to None
    fast.next = None


'''
Let n be the number of distinct reachable nodes.
Time: O(n): cycle detection takes O(n), then locating the predecessor
of the loop's entry takes at most another O(n). Adding passes stays O(n).
Space: O(1) auxiliary: only pointers and a boolean are used; the loop
is removed by changing one existing next link.
'''
