# Function to find the starting point of the loop
def findLoopStart(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    # Step 1: Detect if there's a loop in the list
    hasCycle = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            hasCycle = True
            break
    # If there's no cycle, return None
    if not hasCycle:
        return None
    # Step 2: Find the starting point of the loop
    # Reset slow pointer to the head
    slow = head
    while slow is not fast:
        # Move both pointers one step at a time
        slow = slow.next
        fast = fast.next
    # The point where slow and fast meet again is the starting point of the loop
    return slow


'''
Let n be the number of distinct reachable nodes.
Time: O(n): Floyd's detection needs O(n) steps. Resetting slow to head
and advancing both pointers to the entry takes at most another O(n).
Space: O(1) auxiliary: only two pointers and a cycle flag are stored.
'''
