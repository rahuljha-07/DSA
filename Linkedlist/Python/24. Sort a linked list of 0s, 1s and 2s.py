class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Function to sort a linked list of 0s, 1s, and 2s using counting
def segregate(head):
    count = [0, 0, 0]
    temp = head
    # Count the occurrences of 0, 1, and 2 in the list
    while temp:
        # Increment the count of the respective data
        count[temp.data] += 1
        temp = temp.next
    temp = head
    i = 0
    # Update the linked list based on the counts
    while temp:
        if count[i] == 0:
            # Move to the next number if no more of the current number is left to assign
            i += 1
        else:
            # Set the node's data to the current number
            temp.data = i
            # Decrease the count for the current number
            count[i] -= 1
            # Move to the next node
            temp = temp.next
    # Return the head of the modified list
    return head


# Function to sort a linked list of 0s, 1s, and 2s using dummy nodes
def segregateUsingDummy(head):
    # Create dummy nodes for 0, 1, and 2
    # Dummy node to store 0s
    zeroDummy = Node(0)
    # Dummy node to store 1s
    oneDummy = Node(0)
    # Dummy node to store 2s
    twoDummy = Node(0)
    zero = zeroDummy
    one = oneDummy
    two = twoDummy
    # Pointer to traverse the original list
    curr = head
    # Traverse the original list and divide nodes into 0, 1, and 2 lists
    while curr:
        if curr.data == 0:
            # Add node to the zero list
            zero.next = curr
            # Move the zero pointer
            zero = zero.next
        elif curr.data == 1:
            # Add node to the one list
            one.next = curr
            # Move the one pointer
            one = one.next
        else:
            # Add node to the two list
            two.next = curr
            # Move the two pointer
            two = two.next
        # Move to the next node in the original list
        curr = curr.next
    # Terminate the three lists
    # Last node of the two list should point to None
    two.next = None
    # Skip an empty one-list rather than disconnecting the two-list.
    zero.next = oneDummy.next if oneDummy.next else twoDummy.next
    # Link the one list to the two list
    one.next = twoDummy.next
    # The head of the sorted list is the next node of the zero dummy node
    sortedHead = zeroDummy.next
    # Return the head of the sorted linked list
    return sortedHead


'''
Let n be the number of nodes; data must be 0, 1, or 2.
Counting time: O(n): one pass counts values, one pass overwrites data,
and i advances only twice. Space: O(1) auxiliary for exactly three counters.
Dummy-list time: O(n): one pass separates nodes, then O(1) links join them.
Space: O(1) auxiliary: exactly three dummy nodes and a fixed set of pointers.
Neither approach allocates a new n-node result list.
'''
