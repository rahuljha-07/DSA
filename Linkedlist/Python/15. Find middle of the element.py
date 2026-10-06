# Function to find the middle of the linked list using slow and fast pointers
def findMiddle(head):
    # Check if the list is empty
    if head is None:
        return -1
    # Initialize two pointers: slow and fast
    slow = head
    fast = head
    # Traverse the list with fast moving two steps at a time and slow moving one step at a
    # time
    while fast and fast.next:
        # Move slow pointer one step
        slow = slow.next
        # Move fast pointer two steps
        fast = fast.next.next
    # When fast reaches the end, slow will be at the middle
    # Return the data of the middle node
    return slow.data


'''
Let n be the number of nodes.
Time: O(n): fast crosses the list in about n/2 iterations, while slow
moves one node per iteration. For even n, it returns the second middle.
Space: O(1) auxiliary: only slow and fast pointers are stored.
'''
