# Function to move the last element to the front of the linked list
def moveLastToFront(head):
    if head is None or head.next is None:
        return head
    secondLast = None
    last = head
    # Traverse the list to find the last and second-last nodes
    while last.next is not None:
        secondLast = last
        last = last.next
    # If there are two nodes, make the second-last node's next point to None
    secondLast.next = None
    # Make the last node point to the head
    last.next = head
    # Move the head pointer to the last node
    head = last
    return head


'''
Let n be the number of nodes.
Time: O(n): finding the last and second-last nodes requires one traversal;
the final pointer updates take O(1).
Space: O(1) auxiliary: only two pointers are needed and nodes are reused.
'''
