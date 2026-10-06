class Node:
    # Constructor to initialize the node
    def __init__(self, val):
        self.data = val
        self.next = None
        self.random = None


# Function to clone a linked list with next and random pointers
def cloneList(head):
    # If the list is empty, return None
    if head is None:
        return None
    # Step 1: Create a cloned linked list with data and next pointers, but random pointers
    # are None
    # Head of the cloned list
    cloneHead = None
    # Current pointer for the cloned list
    cloneCurr = None
    # Current pointer for the original list
    curr = head
    # Create the cloned list (copying nodes with data and None random pointers)
    while curr:
        # Create a new node for the cloned list
        newNode = Node(curr.data)
        if cloneHead is None:
            # Initialize the cloned list head
            cloneHead = cloneCurr = newNode
        else:
            # Append to the cloned list
            cloneCurr.next = newNode
            # The C++ source omitted this assignment.
            cloneCurr = cloneCurr.next
        # Move to the next node in the original list
        curr = curr.next
    # Step 2: Set the next and random pointers of the cloned list
    # Reset the current pointer to the head of the original list
    curr = head
    # Reset the cloned current pointer to the head of the cloned list
    cloneCurr = cloneHead
    while curr:
        # Store the address of the next node in the original list
        temp = curr.next
        # Point the original node's next to the cloned node
        curr.next = cloneCurr
        # Point the cloned node's random to the original node
        cloneCurr.random = curr
        curr = temp
        # Move to the next node in the cloned list
        cloneCurr = cloneCurr.next
    # Step 3: Fix the random pointers of the cloned list
    # Reset to the head of the original list
    curr = head
    # Reset to the head of the cloned list
    cloneCurr = cloneHead
    while cloneCurr:
        # Update the cloned node's random pointer to point to the correct cloned node
        cloneCurr.random = (cloneCurr.random.random.next
                            if cloneCurr.random.random else None)
        cloneCurr = cloneCurr.next
    # Return the head of the cloned list
    return cloneHead


'''
Let n be the number of nodes; random must point inside the list or be None.
Time: O(n): three passes create nodes, map originals to clones using
next links, and translate random links. Each pass does O(1) work per node.
Space: O(1) auxiliary for traversal pointers; O(n) output for cloned nodes.
Source behavior is preserved: original next links are overwritten to point
to clones and are NOT restored. No dictionary or extra n-node mapping
is introduced.
'''
