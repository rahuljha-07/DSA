class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Function to rearrange nodes in the list so that all even nodes appear before odd nodes
def divide(N, head):
    if not head or not head.next:
        return head
    # Dummy nodes to start the even and odd lists
    # Dummy head for even numbers
    evenDummy = Node(0)
    # Dummy head for odd numbers
    oddDummy = Node(0)
    # Pointer to build the even list
    even = evenDummy
    # Pointer to build the odd list
    odd = oddDummy
    # Pointer to traverse the original list
    current = head
    # Traverse the list and separate nodes into even and odd lists
    while current:
        if current.data % 2 == 0:
            # Link even node
            even.next = current
            # Move even pointer forward
            even = even.next
        else:
            # Link odd node
            odd.next = current
            # Move odd pointer forward
            odd = odd.next
        # Move to the next node
        current = current.next
    # Connect the end of even list to the start of odd list
    even.next = oddDummy.next
    # End the odd list
    odd.next = None
    # Update head to point to the start of the new list (first even node)
    head = evenDummy.next
    return head


'''
Let n be the actual number of nodes; N is unused, as in the source.
Time: O(n): each node is visited once and attached to either the even
or odd chain in O(1); joining the chains is also O(1).
Space: O(1) auxiliary: two dummy nodes and a fixed number of pointers.
Original nodes are reused, preserving order within each parity group.
'''
