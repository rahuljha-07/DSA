# Function to remove duplicates from an unsorted linked list using a set
def removeDuplicates(head):
    # Return None if the list is empty
    if head is None:
        return None
    seen = set()
    current = head
    # Start from the next node after head
    nextNode = head.next
    # Push the head's data into the set
    seen.add(current.data)
    # Traverse the list starting from the second node
    while nextNode is not None:
        if nextNode.data in seen:
            # Skip the duplicate node
            current.next = nextNode.next
        else:
            # Add current data to the set
            seen.add(nextNode.data)
            # Move current pointer forward
            current = nextNode
        # Move nextNode to the next node
        nextNode = nextNode.next
    # Return the modified list
    return head


'''
Let n be the number of nodes and u the number of unique values.
Time: O(n) expected: each node is visited once, and set membership/insertion
takes O(1) on average. Pathological hash collisions can make it O(n^2).
Space: O(u), at most O(n), auxiliary: seen stores each unique value once.
No new result nodes are created.
'''
