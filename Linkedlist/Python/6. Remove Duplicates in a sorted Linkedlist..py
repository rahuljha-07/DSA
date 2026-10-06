# Function to remove duplicates from a sorted linked list
def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    # Initialize two pointers:
    # 'current' points to the node currently being checked for duplicates
    # 'nextNode' is the node following 'current', which we compare with 'current'
    current = head
    nextNode = head.next
    # Traverse the list until we reach the end
    while nextNode is not None:
        if current.data != nextNode.data:
            current = nextNode
            nextNode = nextNode.next
        else:
            # If 'current' and 'nextNode' have the same data, there's a duplicate
            # Skip the duplicate by changing 'current's next pointer to the node after
            # 'nextNode'
            current.next = nextNode.next
            # Move 'nextNode' to the next node in the list
            nextNode = current.next
    # Return the head of the modified list
    return head


'''
Let n be the number of nodes; the input must be sorted.
Time: O(n): nextNode advances to the following node on every iteration.
Adjacent equal values can be removed without searching the rest of the list.
Space: O(1) auxiliary: two pointers suffice; existing links are changed
and no collection or new list is allocated.
'''
