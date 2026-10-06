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


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Function to split the circular linked list into two halves
def splitList(head):
    if head is None or head.next is None:
        return
    # Step 1: Remove the loop if present
    removeLoop(head)
    # Step 2: Initialize slow and fast pointers to find the middle of the list
    slow = head
    fast = head
    # Traverse the list to find the middle using slow and fast pointers
    while fast is not None and fast.next is not None:
        # Move fast pointer two steps at a time
        fast = fast.next.next
        # Move slow pointer one step at a time
        slow = slow.next
    # At this point, slow points to the middle of the list
    secondHalf = slow.next
    # End the first half of the list
    slow.next = None
    # Step 3: Print the two halves (or return them if needed)
    # Optionally: If you need to return the two halves, you can return head (first half) and
    # secondHalf (second half)
    # For now, let's just print the two halves for demonstration
    print("First half: ", end="")
    printList(head)
    print("Second half: ", end="")
    printList(secondHalf)


'''
Let n be the number of distinct reachable nodes.
Time: O(n): removing the cycle, finding the midpoint, and printing both
parts each cost at most O(n); a fixed number of passes is still linear.
Space: O(1) auxiliary: all steps are iterative and reuse existing nodes.
Source behavior is preserved: it removes the circle and prints linear
parts, splitting AFTER the second middle for even lengths. It does not
produce two circular lists or necessarily two equally sized halves.
'''
