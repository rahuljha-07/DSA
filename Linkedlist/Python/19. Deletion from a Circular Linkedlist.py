def deleteNode(head, value):
    # If the list is empty, nothing to delete
    if head is None:
        return head
    if head.next is head and head.data == value:
        # Set head to None as the list is now empty
        head = None
        return head
    temp = head
    prev = None
    if head.data == value:
        last = head
        # Traverse the list to find the last node
        while last.next is not head:
            last = last.next
        # Update the last node's next to the second node
        last.next = head.next
        # Move head to the next node and delete the old head
        # Loop back to the head if we haven't reached the end
        temp = head
        head = head.next
        return head
    while True:
        if temp.data == value:
            # Skip the node to delete
            prev.next = temp.next
            return head
        prev = temp
        temp = temp.next
        if temp is head:
            break
    return head


'''
Let n be the number of nodes in a list circular back to head.
Time: O(n) worst case: finding the tail when deleting head or searching
for value visits at most one complete circle. Unlinking takes O(1).
Space: O(1) auxiliary: only pointers are used; no new nodes are created.
Return the updated head because Python has no C++ Node*& parameter.
'''
